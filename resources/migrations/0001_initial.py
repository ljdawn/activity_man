# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u6742\u5fd7\u540d\u79f0')),
                ('price', models.FloatField(max_length=6, verbose_name='\u4ef7\u683c')),
                ('volume', models.CharField(max_length=1000, verbose_name='\u671f\u520a\u7f16\u53f7')),
                ('description', models.CharField(max_length=1000, verbose_name='\u6742\u5fd7\u7b80\u4ecb')),
                ('created_by', models.ForeignKey(verbose_name='\u521b\u5efa\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6742\u5fd7',
                'verbose_name_plural': '\u6742\u5fd7',
            },
        ),
    ]
