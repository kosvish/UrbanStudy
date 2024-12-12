from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base


class Author(Base):
    __tablename__ = "authors"
    # __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=True)

    books = relationship("Book", back_populates="author")


# OneToMany OneToOne ManyToMany (m2m), ManyToOne,\

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")
