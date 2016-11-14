# coding:utf-8
from django.shortcuts import render, HttpResponse


def helloworld(request):
    return HttpResponse("<h1>Hello Django World... </h1>")


def index(request):

    userinfo = {"username": "张三丰", "age": 50, "addr": "武当山"}

    persons = ["王小明", "李守财", "张富贵"]

    return render(request, template_name='firstapp/index.html',
                  context={"user": userinfo, "persons": persons, "string": "我是一个字符串"})
