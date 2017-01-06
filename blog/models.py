#coding:utf-8

from __future__ import unicode_literals
from django.db import models

class BaseModel(models.Model):
	create_date = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
	update_date = models.DateTimeField(auto_now=True,verbose_name='修改时间')

	class Meta:
		abstract=True

class UserInfo(BaseModel):
	username = models.CharField(max_length=20,verbose_name='用户名')
	passwd = models.CharField(max_length=20,verbose_name='用户密码')
	avatar = models.ImageField(verbose_name="头像",blank=True)
	signature = models.CharField(max_length=200,verbose_name='个性签名',blank=True)


class BlogInfo(BaseModel):
	title = models.CharField(max_length=50,verbose_name='博客标题')
	content = models.TextField(verbose_name='博客内容')
	author = models.ForeignKey(UserInfo,verbose_name='作者')


class Comment(BaseModel):
	blogInfo = models.ForeignKey(BlogInfo,verbose_name='回复博客')
	msg = models.TextField(verbose_name='回复内容')
	userInfo = models.ForeignKey(UserInfo,verbose_name='撰写回复的用户')
	#target_userInfo = models.ForeignKey(UserInfo,verbose_name='回复目标用户')

