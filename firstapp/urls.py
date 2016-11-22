# coding:utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.helloworld),
    url(r'^index$', views.index),
    url(r'^user_add$', views.user_add, name="user_add"),
    url(r'^user_list$', views.user_list, name="user_list"),
    url(r'^user_delete/([0-9])$', views.user_delete, name="user_delete"),
]
