from django.urls import path
from .views import handle_requests

urlpatterns = [
    path('handle/', handle_requests, name='handle_requests'),
]
