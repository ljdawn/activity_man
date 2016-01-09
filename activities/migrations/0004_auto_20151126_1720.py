# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import activities.models
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_auto_20151121_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='created_time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='dead_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='activity',
            name='draw_desc',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='activity',
            name='exchange_ddl',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='magazine',
            field=models.ForeignKey(to='resources.Magazine'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '\u7b79\u5907'), (1, '\u9001\u5ba1'), (2, '\u5c31\u7eea'), (3, '\u8fdb\u884c\u4e2d'), (4, '\u5df2\u5b8c\u6210')]),
        ),
        migrations.AlterField(
            model_name='activity',
            name='winning_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='publish',
            name='activity',
            field=models.ForeignKey(to='activities.Activity'),
        ),
        migrations.AlterField(
            model_name='publish',
            name='draw_desc',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='publish',
            name='magazine',
            field=models.ForeignKey(to='resources.Magazine'),
        ),
        migrations.AlterField(
            model_name='publish',
            name='winning_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='question',
            name='activity',
            field=models.ForeignKey(to='activities.Activity'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=2, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_a',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_b',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_c',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_d',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=tinymce.models.HTMLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='report',
            name='accept_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='cell',
            field=models.CharField(max_length=11, validators=[activities.models.validate_cell]),
        ),
        migrations.AlterField(
            model_name='report',
            name='level',
            field=models.SmallIntegerField(choices=[(0, '\u672a\u4e2d\u5956'), (1, '\u4e00\u7b49\u5956'), (2, '\u4e8c\u7b49\u5956'), (3, '\u4e09\u7b49\u5956')]),
        ),
        migrations.AlterField(
            model_name='report',
            name='lucky_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
