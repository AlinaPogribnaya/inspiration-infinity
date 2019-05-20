from django.shortcuts import render
from django import template

# Create your views here.
from django.http import HttpResponse

def home(request): return render(request, 'templates/static_handler.html')
