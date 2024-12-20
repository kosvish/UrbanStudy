# Установите Django:

```bash
pip install django
```

### Создайте новый проект:

```bash
django-admin startproject book_project
cd book_project
Создайте новое приложение:
```

### Создайте новое приложение:

```bash
python manage.py startapp books
```

# Шаг 2: Urls и View. Функциональное и классовые представления в Django

Внутри приложения books создайте папку templates и внутри нее папку books. Внутри папки books создайте два файла:
class_template.html и func_template.html.
В views.py приложения books добавьте функциональное и классовое представление:

```python
from django.shortcuts import render
from django.views import View


def func_view(request):
    return render(request, 'books/func_template.html')


class ClassView(View):
    def get(self, request):
        return render(request, 'books/class_template.html')
```

3. В urls.py приложения books добавьте маршруты:

```python
from django.urls import path
from .views import func_view, ClassView

urlpatterns = [
    path('func/', func_view, name='func_view'),
    path('class/', ClassView.as_view(), name='class_view'),
]
```

4. Подключите маршруты приложения к основному urls.py проекта:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
]
```

### Шаг 3: Базовые HTML теги в шаблонах

1. Создайте три HTML файла: index.html, page1.html, page2.html в папке templates/books.
2. В index.html добавьте ссылки на вторичные страницы:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Главная страница</title>
</head>
<body>
<h1>Главная страница</h1>
<a href="{% url 'page1' %}">Страница 1</a>
<a href="{% url 'page2' %}">Страница 2</a>
</body>
</html>
```

3. В page1.html и page2.html добавьте ссылки на главную страницу:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Страница 1</title>
</head>
<body>
<h1>Страница 1</h1>
<a href="{% url 'index' %}">Главная страница</a>
</body>
</html>
```

4. В views.py добавьте представления для этих страниц:

```python
def index(request):
    return render(request, 'books/index.html')


def page1(request):
    return render(request, 'books/page1.html')


def page2(request):
    return render(request, 'books/page2.html')
```

5. В urls.py приложения books добавьте маршруты:

```python
urlpatterns = [
    path('', index, name='index'),
    path('page1/', page1, name='page1'),
    path('page2/', page2, name='page2'),
    path('func/', func_view, name='func_view'),
    path('class/', ClassView.as_view(), name='class_view'),
]
```

# Шаг 4: DTL (Django Template Language)

1. Создайте базовый шаблон base.html в папке templates/books:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Мой сайт{% endblock %}</title>
</head>
<body>
<header>
    <h1>Мой сайт о книгах</h1>
    <nav>
        <a href="{% url 'index' %}">Главная</a>
        <a href="{% url 'page1' %}">Страница 1</a>
        <a href="{% url 'page2' %}">Страница 2</a>
    </nav>
</header>
<main>
    {% block content %}
    {% endblock %}
</main>
<footer>
    <p>&copy; 2023 Мой сайт о книгах</p>
</footer>
</body>
</html>
```

2. Наследуйте base.html в index.html, page1.html и page2.html:

```html
{% extends 'books/base.html' %}

{% block title %}Главная страница{% endblock %}

{% block content %}
<h1>Главная страница</h1>
<p>Добро пожаловать на наш сайт о книгах!</p>
{% endblock %}
```

```html
{% extends 'books/base.html' %}

{% block title %}Страница 1{% endblock %}

{% block content %}
<h1>Страница 1</h1>
<p>Информация о странице 1.</p>
{% endblock %}
```

```html
{% extends 'books/base.html' %}

{% block title %}Страница 2{% endblock %}

{% block content %}
<h1>Страница 2</h1>
<p>Информация о странице 2.</p>
{% endblock %}
```

# Шаг 5: HTTP ответы. GET, POST запросы в Django

1. Создайте новое приложение для демонстрации GET и POST запросов:

```bash
python manage.py startapp requests
```

2. В views.py приложения requests добавьте представление для обработки GET и POST запросов:

```python
from django.shortcuts import render
from django.http import HttpResponse


def handle_requests(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        return HttpResponse(f'Received POST data: {data}')
    else:
        data = request.GET.get('data')
        return HttpResponse(f'Received GET data: {data}')
```

3. В urls.py приложения requests добавьте маршрут:

```python
from django.urls import path
from .views import handle_requests

urlpatterns = [
    path('handle/', handle_requests, name='handle_requests'),
]
```

4. Подключите маршруты приложения requests к основному urls.py проекта:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('requests/', include('requests.urls')),
]
```

# Шаг 6: Формы отправки данных. HTML и Django формы

1. Создайте новое приложение для демонстрации форм:

```bash
python manage.py startapp forms
```

2. В forms.py приложения forms создайте форму:

```python
from django import forms


class BookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    author = forms.CharField(label='Author', max_length=100)
```

3. В views.py приложения forms добавьте представление для обработки формы:

```python
from django.shortcuts import render
from .forms import BookForm


def book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            return HttpResponse(f'Book title: {title}, Author: {author}')
    else:
        form = BookForm()
    return render(request, 'forms/book_form.html', {'form': form})
```

4. В urls.py приложения forms добавьте маршрут:

```python
from django.urls import path
from .views import book_form

urlpatterns = [
    path('books/', book_form, name='book_form'),
]
```

5. Подключите маршруты приложения forms к основному urls.py проекта:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('requests/', include('requests.urls')),
    path('forms/', include('forms.urls')),
]
```

6. Создайте шаблон book_form.html в папке templates/forms:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Book Form</title>
</head>
<body>
<h1>Book Form</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
</body>
</html>
```