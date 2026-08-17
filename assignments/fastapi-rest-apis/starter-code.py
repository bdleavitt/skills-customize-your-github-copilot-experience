"""Starter code for the Building REST APIs with FastAPI assignment."""

from typing import Optional

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Mergington Library API")


class Book(BaseModel):
    """A book stored by the API."""

    id: int
    title: str
    author: str
    year: int


class BookUpdate(BaseModel):
    """Fields that may be changed on an existing book."""

    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None


books: list[Book] = []


@app.get("/")
def read_root() -> dict[str, str]:
    """Return a welcome message."""

    return {"message": "Welcome to the Mergington Library API"}


@app.get("/books")
def list_books() -> list[Book]:
    """Return all books."""

    # TODO: Return the in-memory collection.
    raise NotImplementedError


@app.get("/books/{book_id}")
def get_book(book_id: int) -> Book:
    """Return the book with the requested ID."""

    # TODO: Find and return the book, or raise a 404 HTTPException.
    raise NotImplementedError


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: Book) -> Book:
    """Add a new book to the collection."""

    # TODO: Reject duplicate IDs with a 409 HTTPException.
    # TODO: Store and return the new book.
    raise NotImplementedError


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, changes: BookUpdate) -> Book:
    """Update fields on an existing book."""

    # TODO: Find the book or raise a 404 HTTPException.
    # TODO: Apply only the fields supplied in changes and return the book.
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> Response:
    """Remove an existing book."""

    # TODO: Find and remove the book, or raise a 404 HTTPException.
    # A successful deletion should return Response(status_code=204).
    raise NotImplementedError
