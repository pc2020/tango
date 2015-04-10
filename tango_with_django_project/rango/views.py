from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world wide web! Here is the <a href='/rango/about' />about page</a>")
