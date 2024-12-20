from django.urls import path
from .views import func_view, ClassView, page1, page2, index, get_all_books




urlpatterns = [
    path('', index, name='index'),
    path('page1/', page1, name='page1'),
    path('page2/', page2, name='page2'),
    path('func/', func_view, name='func_view'),
    path('class/', ClassView.as_view(), name='class_view'),
    path('all-books/', get_all_books)
]

