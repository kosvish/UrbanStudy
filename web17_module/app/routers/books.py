from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, ScalarResult, update, delete, insert

from app.database import get_db
from app.models import Book, Author
from typing import List, Annotated

from app.schemas import BookCreate

# библиотека для работы с excel в Python
# read_csv()

router = APIRouter()


@router.post("/")
def create_book(book: BookCreate, session: Session = Depends(get_db)):
    # Проверка существования автора
    # session.execute(insert(Book).values(title='123', author_id=1)).one_or_none()
    # session.execute(update(Book).where(Book.id == 1).values(title='1234'))
    # session.execute(delete(Book).where(Book.id == 1))
    # session.commit()
    # session.commit()
    # session.commit()
    # book = session.scalar(select(Book).where(Book.id == 1)) # Book # None
    # book = session.scalars(select(Book).where(Book.id == 1)).one_or_none() # ScalarResult [..., book2, book3, book4]
    # tasks = session.scalars(select(Task).where(Task.user_id == 1)).all()
    # user = session.scalar(select(User).where(User.id == 1))
    # return user.tasks
    # session.query()
    # session.get()
    # session.get_one()

    stmt = select(Author).where(Author.id == book.author_id)
    db_author = session.scalar(stmt)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    db_book = Book(title=book.title, author_id=book.author_id)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book


@router.get("/")
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    stmt = select(Book).offset(skip).limit(limit)
    books = db.scalars(stmt)
    return books


@router.get("/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db)):
    stmt = select(Book).where(Book.id == book_id)
    db_book = db.scalar(stmt)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.put("/{book_id}")
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    stmt = select(Book).where(Book.id == book_id)
    db_book = db.scalars(stmt)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    # Проверка существования автора
    stmt = select(Author).where(Author.id == book.author_id)
    db_author = db.scalar(stmt)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    # db_book.title = book.title
    # db_book.author_id = book.author_id
    db.execute(update(Book).where(Book.id == book_id).values(title=book.title, author_id=book.author_id))
    db.commit()
    db.refresh(db_book)
    return db_book


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    stmt = select(Book).where(Book.id == book_id)
    db_book = db.scalar(stmt)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return db_book
