from fastapi import APIRouter, Request, Form, HTTPException, Query
from fastapi.responses import HTMLResponse
from models.book import Book
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=['Books'])
templates = Jinja2Templates(directory="templates")

books = {}


# Маршрут для главной страницы
@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "books": books})


# Маршрут для создания новой книги

@router.post("/books/", response_class=HTMLResponse)
def create_book(request: Request, title: str = Form(...), author: str = Form(...), price: float = Form(...)):
    book = Book(title=title, author=author, price=price)
    book_id = len(books) + 1
    books[book_id] = book
    return templates.TemplateResponse("book.html", {"request": request, "book": book})


# Маршрут для чтения информации о книге

@router.get("/books/{book_id}", response_class=HTMLResponse, name='current-book')
async def read_book(request: Request, book_id: int):
    book = books.get(book_id)
    if book:
        return templates.TemplateResponse("book.html", {"request": request, "book": book})
    # return True
    return templates.TemplateResponse("error.html", {"request": request, "message": "Book not found"})


# Маршрут для обновления информации о книге

@router.put("/books/{book_id}/", response_class=HTMLResponse)
def update_book(request: Request, book_id: int, title: str = Form(...), author: str = Form(...),
                price: float = Form(...)):
    if book_id in books:
        book = Book(title=title, author=author, price=price)
        books[book_id] = book
        return templates.TemplateResponse("book.html", {"request": request, "book": book})
    return templates.TemplateResponse("error.html", {"request": request, "message": "Book not found"})


# Маршрут для удаления книги


@router.delete("/books/{book_id}", response_class=HTMLResponse)
def delete_book(request: Request, book_id: int):
    if book_id in books:
        del books[book_id]
        return templates.TemplateResponse("index.html", {"request": request, "books": books, "message": "Book deleted"})
    return templates.TemplateResponse("error.html", {"request": request, "message": "Book not found"})
