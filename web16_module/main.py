from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes import books

app = FastAPI()

# REST API

# Настройка шаблонов Jinja2
templates = Jinja2Templates(directory="templates")

# Настройка статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# Включение маршрутов для книг
app.include_router(books.router)


# GET
# POST, PUT, DELETE, HEAD, OPTIONS, PATCH
# 1..  2.. 3.. 4.. 5.. 204 No Content 304 303 404 Not Found 5.. 500 Internal Server Error
# Query Params
# Query Path
# typing
# Аннотации в Python
@app.get('/')
def get_main_page(q: int = 10):
    return 'hello world' * q


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8001)
