from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'content': 'Welcome to Rango!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'content': 'This page was made by Alan'}
    return render(request, 'rango/index.html', context=context_dict)
