import json
from typing import List
from pydantic import BaseModel


class Category(BaseModel):
    id: int = None
    name: str
    slug: str
    image: str = None
    parent_id: int = None


class CategoryTree(Category):
    parents: List[Category]


class NewCategory(BaseModel):
    name: str
    parent: int = None

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class UpdateCategory(BaseModel):
    name: str = None
    slug: str = None
    image: str = None
    parent: int = None

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
