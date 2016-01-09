# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='magazine',
            field=models.ForeignKey(verbose_name='\u6742\u5fd7', to='resources.Magazine'),
        ),
    ]
