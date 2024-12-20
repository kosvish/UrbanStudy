from django.urls import path
from .views import book_form

urlpatterns = [
    path('book/', book_form, name='book_form'),
]
