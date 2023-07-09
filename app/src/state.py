from dataclasses import dataclass
from database.database import Connection
from aioredis import Redis

@dataclass
class State:
    pgdb: Connection = None
    redis: Redis = None


state = State()
