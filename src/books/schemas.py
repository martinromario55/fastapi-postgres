from pydantic import BaseModel

from src.db.models import Book



class BookResponseModel(Book):
    pass


class BookCreateModel(BaseModel):
    title: str
    author: str
    isbn: str
    description: str
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Book Title",
                "author": "John Doe",
                "isbn": "isbn-123-456-789-0",
                "description": "This is a book sample description",
            }
        }
    }