from pydantic import BaseModel


class AuthUser(BaseModel):
    login: str
    password: str = None


class User(BaseModel):
    id: int
    login: str


class TokenData(BaseModel):
    login: str


class Token(BaseModel):
    access_token: str
    token_type: str
