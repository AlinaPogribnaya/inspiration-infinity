from django.shortcuts import render

# Create your views here.
from .models import Article
from django.shortcuts import render
from django.http import Http404

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})
