from typing import Annotated, Union

from fastapi import APIRouter, Depends, Request, Response, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.state import state
from src.models import rec_to_model
from .models import AuthUser, User, TokenData, Token
from .service import create_password_hash, check_password, create_token, get_current_user, SECRET_KEY, ALGORITHM
from .queries import register_user, get_user_credentials, get_user_by_id, get_user
from dependencies.sessions import Session
from jose import JWTError, jwt
from passlib.context import CryptContext
import json
from passlib.hash import pbkdf2_sha256

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)


@router.post('/login', response_model=User)
async def login(request: Request, response: Response, data: AuthUser = None):
    session = Session(request, response)
    from_redis = await session.get_from_redis()
    if not from_redis:
        user = await get_user_credentials(data)
        if check_password(user['password'], data.password):
            await session.set_session()
            await session.to_redis(user['id'])
            return rec_to_model(User, {'id': user['id'], 'login': user['login']})
        else:
            raise HTTPException(status_code=401, detail='Invalid credentials')
    user = await get_user_by_id(int(from_redis))
    return user


@router.post('/register')
async def register(request: Request, data: AuthUser):
    password_hash = create_password_hash(data.password)
    data.password = password_hash
    return await register_user(data)


@router.post('/token', response_model=Token)
async def get_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_user(AuthUser(login=form_data.username, password=form_data.password))
    token = create_token(data={'sub': user.login})
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    response.headers['Authorization'] = 'Bearer ' + token
    return Token(access_token=token, token_type='bearer')


@router.get('/token_check/')
async def asd(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    exp = jwt._validate_exp(payload, 60)
    print(jwt.get_unverified_claims(token))
    print(exp)