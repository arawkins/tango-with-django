from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Rango</h1><ul><li><a href='/rango/'>Home</a></li><li><a href='/rango/about/'>About</a></li><p>Home Page</p>")

def about(request):
    return HttpResponse("<h1>Rango</h1><ul><li><a href='/rango/'>Home</a></li><li><a href='/rango/about/'>About</a></li><p>About Page</p>")
