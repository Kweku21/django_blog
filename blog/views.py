from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home'
    }
    return render(request, template_name='blog/home.html', context=context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, template_name='blog/about.html', context=context)
