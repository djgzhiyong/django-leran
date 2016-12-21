#coding:utf-8
from django.contrib import admin
from models import UserInfo,BlogInfo,Comment

admin.site.register(UserInfo,verbose_name='用户')
admin.site.register(BlogInfo,verbose_name='博客')
admin.site.register(Comment,verbose_name='回复')