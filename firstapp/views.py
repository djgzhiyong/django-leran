from django.shortcuts import render, HttpResponse


def helloworld(request):
    return HttpResponse("<h1>Hello Django World... </h1>")


def index(request):
    return render(request, template_name='firstapp/index.html')
