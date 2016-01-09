# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import activities.models
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u6d3b\u52a8\u540d\u79f0')),
                ('description', models.CharField(max_length=1000, verbose_name='\u63cf\u8ff0')),
                ('created_time', models.DateField(auto_now_add=True, verbose_name='\u521b\u5efa\u65e5\u671f')),
                ('start_time', models.DateField(verbose_name='\u5f00\u59cb\u65e5\u671f')),
                ('dead_time', models.DateField(verbose_name='\u622a\u6b62\u65e5\u671f')),
                ('exchange_ddl', models.DateField(auto_now_add=True, verbose_name='\u5151\u5956\u622a\u6b62\u65e5\u671f')),
                ('winning_no', models.CharField(max_length=10, verbose_name='\u4e2d\u5956\u53f7\u7801')),
                ('draw_desc', models.CharField(default='\u795d\u60a8\u597d\u8fd0', max_length=200, verbose_name='\u5f00\u5956\u8bf4\u660e')),
                ('status', models.SmallIntegerField(verbose_name='\u72b6\u6001', choices=[(0, '\u7b79\u5907'), (1, '\u9001\u5ba1'), (2, '\u5c31\u7eea'), (3, '\u8fdb\u884c\u4e2d'), (4, '\u5df2\u5b8c\u6210')])),
                ('created_by', models.ForeignKey(verbose_name='\u521b\u5efa\u8005', to=settings.AUTH_USER_MODEL)),
                ('magazine', models.OneToOneField(verbose_name='\u6742\u5fd7', to='resources.Magazine')),
            ],
            options={
                'verbose_name': '\u6d3b\u52a8',
                'verbose_name_plural': '\u6d3b\u52a8',
            },
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('winning_no', models.CharField(max_length=10, verbose_name='\u4e2d\u5956\u53f7\u7801')),
                ('draw_desc', models.CharField(default='\u795d\u60a8\u597d\u8fd0', max_length=200, verbose_name='\u5f00\u5956\u8bf4\u660e')),
                ('activity', models.ForeignKey(verbose_name='\u6d3b\u52a8\u540d\u79f0', to='activities.Activity')),
                ('magazine', models.ForeignKey(verbose_name='\u6742\u5fd7\u540d\u79f0', to='resources.Magazine')),
            ],
            options={
                'verbose_name': '\u516c\u5e03\u53f7\u7801',
                'verbose_name_plural': '\u516c\u5e03\u53f7\u7801',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', tinymce.models.HTMLField(max_length=1000, verbose_name='\u9898\u76ee\u63cf\u8ff0')),
                ('answer', models.CharField(max_length=2, verbose_name='\u6b63\u786e\u7b54\u6848', choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D')])),
                ('option_a', models.CharField(max_length=100, verbose_name='\u9009\u9879A.')),
                ('option_b', models.CharField(max_length=100, verbose_name='\u9009\u9879B.')),
                ('option_c', models.CharField(max_length=100, verbose_name='\u9009\u9879C.')),
                ('option_d', models.CharField(max_length=100, verbose_name='\u9009\u9879D.')),
                ('activity', models.ForeignKey(verbose_name='\u6d3b\u52a8', to='activities.Activity')),
            ],
            options={
                'verbose_name': '\u9898\u76ee',
                'verbose_name_plural': '\u9898\u76ee',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cell', models.CharField(max_length=11, verbose_name='\u8054\u7cfb\u7535\u8bdd', validators=[activities.models.validate_cell])),
                ('level', models.SmallIntegerField(verbose_name='\u7b49\u7ea7', choices=[(0, '\u672a\u4e2d\u5956'), (1, '\u4e00\u7b49\u5956'), (2, '\u4e8c\u7b49\u5956'), (3, '\u4e09\u7b49\u5956')])),
                ('lucky_no', models.IntegerField(verbose_name='\u5e78\u8fd0\u6570\u5b57')),
                ('accept_time', models.DateField(verbose_name='\u9886\u5956\u65f6\u95f4')),
                ('user', models.ForeignKey(verbose_name='\u59d3\u540d', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6d3b\u52a8\u62a5\u8868',
                'verbose_name_plural': '\u6d3b\u52a8\u62a5\u8868',
            },
        ),
    ]
