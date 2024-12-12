from fastapi import FastAPI
import uvicorn
from app.database import engine
from app.routers import authors, books
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(authors.router, prefix="/authors", tags=["authors"])
app.include_router(books.router, prefix="/books", tags=["books"])

# if __name__ == '__main__':
#     uvicorn.run("app")
