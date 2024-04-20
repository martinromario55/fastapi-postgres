from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg

from uuid import UUID, uuid4
from datetime import datetime


class Book(SQLModel, table=True):
    __tablename__ = 'books'
    
    
    uid: UUID = Field(sa_column=Column(pg.UUID, default=uuid4, primary_key=True, unique=True))
    title: str = Field(max_length=255)
    author: str = Field(max_length=255)
    isbn: str = Field(max_length=255)
    description: str = Field(max_length=255)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))
    
    
    def __repr__(self) -> str:
        return f"Book => {self.title}"