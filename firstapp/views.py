from django.shortcuts import render, HttpResponse


def helloworld(request):
    return HttpResponse("<h1>Hello Django World... </h1>")
