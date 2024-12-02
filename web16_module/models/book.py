from fastapi import Query
from pydantic import BaseModel, Field
from typing import Annotated


# Определение модели данных для книги с использованием Pydantic
class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)  # Название книги
    author: str = Field(..., min_length=1, max_length=100)  # Автор книги
    price: float = Field(..., gt=0)  # Цена книги #ge le lt

# class Book(BaseModel):
#     title: str
#     author: str
#     price: float
