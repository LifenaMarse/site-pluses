from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "Востребованность", 'url_name': 'demand'},
        {'title': "География", 'url_name': 'geography'},
        {'title': "Навыки", 'url_name': 'skills'},
        {'title': "Последние вакансии", 'url_name': 'latest'}]


def returner(request):
    posts = Main.objects.all()
    context = {'menu': menu,
               'posts': posts,
               'title': 'C/C++ программист'}
    return render(request, 'mainpage/returner.html', context=context)


def demand(request):
    posts = Demand.objects.all()
    return render(request, 'mainpage/demand.html', {'posts': posts, 'menu': menu, 'title': 'Востребованность'})


def geography(request):
    posts = Geography.objects.all()
    post = Pie.objects.all()
    return render(request, 'mainpage/geography.html', {'posts': posts, 'post': post, 'menu': menu, 'title': 'География'})


def skills(request):
    posts = Skill.objects.all()
    return render(request, 'mainpage/skills.html', {'posts': posts, 'menu': menu, 'title': 'Навыки'})


def latest(request):
    return render(request, 'mainpage/latest.html', {'menu': menu, 'title': 'Последние вакансии'})


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")






