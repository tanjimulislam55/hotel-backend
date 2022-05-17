from typing import Any, Generic, List, Optional, Type, Union, TypeVar
from sqlalchemy.orm import Session, declarative_base
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.sql import select, delete, update, insert

from utils.db import database

Base = declarative_base()

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_one(self, id: str) -> Optional[ModelType]:
        query = select(self.model).where(self.model.id == id)
        return await database.fetch_one(query)

    async def get_many(self, skip: int, limit: int) -> List[ModelType]:
        query = select(self.model).offset(skip).limit(limit)
        return await database.fetch_one(query)
    
    async def create(self, object_in: CreateSchemaType) -> int:
        query = insert(self.model).values(**object_in.dict())
        return await database.execute(query)