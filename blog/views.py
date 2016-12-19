from django.shortcuts import render
from django.http import request, response


def index(request):
    return render(request, "blog/index.html")
