from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
books = []

class Book(BaseModel):
    title: str
    author: str

@app.get("/books")
def get_books():
    return []

@app.post("/books")
def create_book(book: Book):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author
    }

    books.append(new_book)
    return new_book
