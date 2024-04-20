from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import text, SQLModel, select

from src.db.models import Book
from .schemas import BookCreateModel

class BookService:
    def __init__(self, session: AsyncSession):
        self.session = session
        
        
    # Get All books
    async def get_all_books(self):
        statement = select(Book).order_by(Book.created_at)
        
        result = await self.session.exec(statement)
        
        return result.all()
    
    # Create Book
    async def create_book(self, book__data: BookCreateModel):
        new_book = Book(**book__data.model_dump())
        
        self.session.add(new_book)
        await self.session.commit()
        
        return new_book
    
    
    # Get a book
    async def get_book(self, book_uid: str):
        statement = select(Book).where(Book.uid == book_uid)
        
        result = await self.session.exec(statement)
        
        return result.first()
    
    # Update a book
    async def update_book(self, book_uid: str, book_update_data: BookCreateModel):
        statement = select(Book).where(Book.uid == book_uid)
        
        result = await self.session.exec(statement)
        
        book = result.first()
        
        for key,value in book_update_data.model_dump().items():
            setattr(book, key, value)
        
        await self.session.commit()
        
        return book
        

    # Delete a book
    async def delete_book(self, book_uid: str):
        statement = select(Book).where(Book.uid == book_uid)
        
        result = await self.session.exec(statement)
        
        book = result.first()
        
        await self.session.delete(book)
        await self.session.commit()