from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.db.main import init_db
from src.books.routes import book_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting")
    await init_db()
    yield
    print("Server is shutting down")


app = FastAPI(
    title="Book Service",
    description="FastAPI with postgres",
    version="0.1.0",
    docs_url="/",
    redoc_url="/redoc",
    lifespan=lifespan
)


app.include_router(book_router)