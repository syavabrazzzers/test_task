from enum import Enum
from typing import List

from pydantic import BaseModel


class StatusCode(int, Enum):
    ok = 200
    created = 201
    badRequest = 400
    unauthorized = 401
    forbidden = 403
    notFound = 404
    notAllowed = 405
    timeout = 408
    teapot = 418
    error = 500
    badGateway = 502


class ResponseModel(BaseModel):
    message: str
    data: list | dict | str | int
    status_code: StatusCode


class ServiceOrders(Enum):
    object = 'object'
    direction = 'direction'
    service = 'service'


class OrderTypes(Enum):
    asc = 'asc'
    desc = 'desc'


class ServiceMappingItem(BaseModel):
    id: int
    object: str
    direction: str
    service: str


class ServiceMappingResponse(BaseModel):
    length: int
    services: List[ServiceMappingItem]


class ServiceMappingUpdate(BaseModel):
    direction_id: int = None
    service_id: int = None


class ServiceMappingCreate(BaseModel):
    object_id: int
    direction_id: int
    service_id: int


class Bush(BaseModel):
    id: int
    name: str

class Object(BaseModel):
    id: int
    name: str
    code: str


class BushMapping(BaseModel):
    id: int
    object: Object
    bush: Bush


class BushMappingCreate(BaseModel):
    object_id: int
    bush_id: int