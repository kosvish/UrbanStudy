from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookForm


def book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            price = form.cleaned_data['price']
            return HttpResponse(f'Book title: {title}, Author: {author} Price: {price}')
    else:
        form = BookForm()

    return render(request, 'forms/book_form.html', {'form': form})
