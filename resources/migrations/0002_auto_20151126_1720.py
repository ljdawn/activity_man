# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='price',
            field=models.FloatField(max_length=6),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='volume',
            field=models.CharField(max_length=1000),
        ),
    ]
