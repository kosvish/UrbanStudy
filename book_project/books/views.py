from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def func_view(request):
    return render(request, 'books/func_template.html')


class ClassView(View):

    def get(self, request):
        return render(request, 'books/class_template.html')


class ClassViewTemplate(TemplateView):
    template_name = 'books/class_template.html'


def index(request):
    return render(request, 'books/index.html')


def page1(request):
    return render(request, 'books/page1.html')


def page2(request):
    return render(request, 'books/page2.html')


def get_all_books(request):
    books_list = ['Доктор Живаго', 'Преступление и наказание', 'Евгений Онегин']
    return render(request, 'books/all_books.html', {"books123": books_list})
