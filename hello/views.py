from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
        return HttpResponse("Hello, world!")

def Jake(request):
        return HttpResponse("Hello, Jake")

def Brian(request):
        return HttpResponse("Hello, Brian")

def greet(request, name):
        return HttpResponse(f"Hello, {name.capitalize()}. Welcome to this website."
                )