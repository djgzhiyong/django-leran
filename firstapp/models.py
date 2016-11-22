# coding:utf-8
from __future__ import unicode_literals

from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=20)  # 用户名字段
    password = models.CharField(max_length=20)  # 用户密码字段
    age = models.IntegerField()  # 用户年龄字段

    def __unicode__(self):
        return self.userName
