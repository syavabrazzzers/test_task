import hashlib
from datetime import timedelta, datetime

from fastapi import Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError
from .models import TokenData, AuthUser

from decouple import config

from .queries import get_user

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(config('ACCESS_TOKEN_EXPIRE_MINUTES'))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_password_hash(password: str) -> str:
    pwd_context.hash(password)
    return pwd_context.hash(password)


def check_password(password: str, hash: str) -> bool:
    return pwd_context.verify(password, hash)


def check_session(request: Request):
    session = request.cookies.get('session')
    return session


def create_token(data: dict):
    to_encode = data.copy()
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    if expires:
        expire = datetime.utcnow() + expires
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(request: Request):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if not request.headers.get('authorization'):
        raise credentials_exception
    token = request.headers.get('authorization').split()[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        login: str = payload.get("sub")
        if login is None:
            raise credentials_exception
        return await get_user(AuthUser(login=login))
    except JWTError:
        raise credentials_exception


