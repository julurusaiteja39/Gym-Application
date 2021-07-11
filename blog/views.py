from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def excercise(request):
    return render(request, 'blog/excercise.html', {'title': 'excercise'})


def nutrition(request):
    return render(request, 'blog/nutrition.html', {'title': 'nutrition'})

# def register(request):
#     return render(request, 'blog/register.html', {'title': 'Register'})
