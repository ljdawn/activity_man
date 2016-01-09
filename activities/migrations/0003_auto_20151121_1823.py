# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20151121_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='draw_desc',
            field=models.CharField(default='\u8bf7\u6293\u7d27\u65f6\u95f4\u5151\u5956', max_length=200, verbose_name='\u5f00\u5956\u8bf4\u660e'),
        ),
    ]
