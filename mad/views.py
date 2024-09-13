from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'a': 1}
    return render(request, "mad/index.html", context)


def rooms(request):
    context = {'a': 1}
    return render(request, "mad/rooms.html", context)


def rent(request):
    return HttpResponse('hello')


def sale(request):
    return HttpResponse('hello')
