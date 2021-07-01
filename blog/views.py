from django.shortcuts import render

posts = [
    {
        'author': 'Kweku Debrah',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'Bismark Debrah',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 30, 2019'
    },
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, template_name='blog/home.html', context=context)


def about(request):
    return render(request, template_name='blog/about.html')
