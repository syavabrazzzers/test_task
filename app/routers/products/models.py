import json

from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    slug: str
    category_id: int
    price: float


class NewProduct(BaseModel):
    name: str
    category_id: int
    price: float

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class UpdateProduct(BaseModel):
    name: str = None
    category_id: int = None
    price: float = None

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class Images(BaseModel):
    product_id: int
    high_quality: str
    medium_quality: str
    low_quality: str


class FullProduct(BaseModel):
    id: int
    name: str
    slug: str
    price: float
    parent_category: str = None
    category: str
    hq_image: str
    mq_image: str
    lq_image: str
