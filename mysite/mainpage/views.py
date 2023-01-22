from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "Востребованность", 'url_name': 'demand'},
        {'title': "География", 'url_name': 'geography'},
        {'title': "Навыки", 'url_name': 'skills'},
        {'title': "Последние вакансии", 'url_name': 'latest'}]


def returner(request):
    context = {'menu': menu,
               'title': 'Главная страница'}
    return render(request, 'mainpage/returner.html', context=context)


def demand(request):
    return render(request, 'mainpage/demand.html', {'menu': menu, 'title': 'Востребованность'})


def geography(request):
    return render(request, 'mainpage/geography.html', {'menu': menu, 'title': 'География'})


def skills(request):
    return render(request, 'mainpage/skills.html', {'menu': menu, 'title': 'Навыки'})


def latest(request):
    return render(request, 'mainpage/latest.html', {'menu': menu, 'title': 'Последние вакансии'})


def categories(request, professionid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{professionid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")






