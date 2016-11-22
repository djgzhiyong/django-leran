# coding:utf-8
from django.shortcuts import render, HttpResponse, redirect
from models import UserInfo


def helloworld(request):
    return HttpResponse("<h1>Hello Django World... </h1>")


def index(request):
    userinfo = {"username": "张三丰", "age": 50, "addr": "武当山"}
    persons = ["王小明", "李守财", "张富贵"]
    return render(request, template_name='firstapp/index.html',
                  context={"user": userinfo, "persons": persons, "string": "我是一个字符串"})


def user_add(request):
    if request.method == "GET":
        return render(request, "firstapp/user_add.html")
    else:
        username = request.POST['username']
        password = request.POST['password']
        age = int(request.POST['age'])

        user = UserInfo(username=username, password=password, age=age)
        user.save()

        return redirect("user_list")


def user_list(request):
    users = UserInfo.objects.all()
    return render(request, "firstapp/user_list.html", {"users": users})


def user_delete(request, user_id):
    u = UserInfo.objects.get(id=user_id)
    if u:
        u.delete()
    return redirect("user_list")
