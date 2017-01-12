# coding:utf-8
from django.shortcuts import render
from django.http import request, response, HttpResponseRedirect

from forms import RegisterForm
from models import UserInfo


def index(request):
    return render(request, "blog/index.html")


def recommend(request):
    return render(request, "blog/recommend.html")


def my(request):
    usertoken = request.session.get("usertoken", None)
    if not usertoken:
        return HttpResponseRedirect("login")
    else:
        return render(request, "blog/my.html")


def login(request):
    if request.method == 'GET':
        return render(request, "blog/login.html")
    else:
        username = request.POST.get("username", None)
        passwd = request.POST.get("passwd", None)
        u = UserInfo.objects.filter(username=username, passwd=passwd)
        if u:
            request.session["usertoken"] = u[0].id
            print "usertoken:{}".format(u[0].id)
            return HttpResponseRedirect("/blog")
        else:
            return render(request, "blog/login.html", {"msg": "登录失败..."})


def register(request):
    if request.method == "GET":
        return render(request, "blog/register.html")
    else:
        register_form = RegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            if UserInfo.objects.filter(username=user.username):
                return render(request, "blog/register.html", {"msg": "用户名已存在..."})
            else:
                user.save()
                return HttpResponseRedirect("login")
        else:
            return render(request, "blog/register.html", {"msg": "用户名&密码输入有误..."})
