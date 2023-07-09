from src.state import state
from .models import AuthUser, User
from src.models import rec_to_model
from passlib.hash import pbkdf2_sha256
from passlib.context import CryptContext
from fastapi import HTTPException


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def register_user(user: AuthUser):
    await state.pgdb.insert(table='users', fields=('login', 'password'), values=(user.login, user.password))


async def get_user_credentials(user: AuthUser):
    user = await state.pgdb.select(table='users', where=f"login='{user.login}'")
    return user[0]


async def get_user_by_id(id: int):
    user = await state.pgdb.select(table='users', columns='id, login', where=f"id={id}")
    return rec_to_model(User, user[0])


async def get_user(user: AuthUser):
    if not user.password:
        current = await state.pgdb.execute(f"select * from users where login='{user.login}'")
        return current
    incorrect_credentials = HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        current = await state.pgdb.execute(f"select login, password from users where login='{user.login}'")
    except:
        raise incorrect_credentials
    if pwd_context.verify(user.password, current[0]['password']):
        return rec_to_model(AuthUser, current[0])
    else:
        raise incorrect_credentials



