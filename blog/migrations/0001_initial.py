# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-12 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('title', models.CharField(max_length=50, verbose_name='\u535a\u5ba2\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u535a\u5ba2\u5185\u5bb9')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('msg', models.TextField(verbose_name='\u56de\u590d\u5185\u5bb9')),
                ('blogInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogInfo', verbose_name='\u56de\u590d\u535a\u5ba2')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('username', models.CharField(max_length=20, verbose_name='\u7528\u6237\u540d')),
                ('passwd', models.CharField(max_length=20, verbose_name='\u7528\u6237\u5bc6\u7801')),
                ('avatar', models.ImageField(blank=True, upload_to='./upload/', verbose_name='\u5934\u50cf')),
                ('signature', models.CharField(blank=True, max_length=200, verbose_name='\u4e2a\u6027\u7b7e\u540d')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='userInfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.UserInfo', verbose_name='\u64b0\u5199\u56de\u590d\u7684\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.UserInfo', verbose_name='\u4f5c\u8005'),
        ),
    ]
