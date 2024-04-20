from fastapi import APIRouter, Depends, status

from sqlmodel.ext.asyncio.session import AsyncSession

from typing import List

from src.db.main import get_session
from .service import BookService
from .schemas import BookCreateModel, BookResponseModel


book_router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


# Get all Books
@book_router.get("/", response_model=List[BookResponseModel])
async def read_root(session: AsyncSession = Depends(get_session)):
    books = await BookService(session).get_all_books()

    return books


# Create a Book
@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(
    book_create_data: BookCreateModel,
    session: AsyncSession = Depends(get_session),
):
    new_book = await BookService(session).create_book(book_create_data)
    
    return new_book


# Get a book
@book_router.get("/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(
    book_id: str,
    session: AsyncSession = Depends(get_session),
):
    book = await BookService(session).get_book(book_id)
    
    return book


# Update book
@book_router.put("/{book_id}", status_code=status.HTTP_200_OK)
async def update_book(
    book_id: str,
    book_update_data: BookCreateModel,
    session: AsyncSession = Depends(get_session),
):
    updated_book = await BookService(session).update_book(book_id, book_update_data)
    
    return updated_book


@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
    book_id: str,
    session: AsyncSession = Depends(get_session),
):
    await BookService(session).delete_book(book_id)
    
    return {}
