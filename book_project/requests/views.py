from django.shortcuts import render
from django.http import HttpResponse


def handle_requests(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        return HttpResponse(f'Received POST data: {data}')
    else:
        data = request.GET.get('data')
        return HttpResponse(f'Received GET data: {data}')
