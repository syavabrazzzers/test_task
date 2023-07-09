import uuid
import hashlib
from pydantic import BaseModel

from fastapi.responses import Response
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from src.state import state


class SessionData(BaseModel):
    key: str
    value: str


class Session:
    def __init__(self, request: Request, response: Response):
        self._session = None
        self._salt = 'salt'
        self.redis = state.redis
        self._request = request
        self._response = response
        self._user_id = None

    @property
    def _hash(self):
        self._session = hashlib.md5(uuid.uuid4().hex.encode() + self._salt.encode()).hexdigest()
        return self._session

    async def set_session(self, token: str = None):
        if token:
            self._response.set_cookie('session', token)
        self._response.set_cookie('session', self._hash)

    @property
    async def get_session(self):
        return self._session

    # @property
    async def get_from_redis(self):
        session = self._request.cookies.get('session')
        if session:
            return await self.redis.get(session)
        return None

    async def to_redis(self, user_id: int):
        self._user_id = user_id
        await self.redis.setex(self._session, 172800, self._user_id) # 172800


async def verify_session(
        request: Request
):
    session = await state.redis.get(request.cookies.get('session')) if request.cookies.get('session') else False
    if session:
        return session
    else:
        raise HTTPException(status_code=401, detail='Unauthorized')
