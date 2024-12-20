from django.contrib import admin
from django.urls import path, include
from books.views import page1
# from book_project.books.views import page1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('requests/', include('requests.urls')),
    path('forms/', include('forms.urls')),
]

# http://127.0.0.1:8000/books/page1
