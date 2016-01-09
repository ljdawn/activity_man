#! /usr/bin/env python
# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from tinymce.models import HTMLField
from resources.models import Magazine
from activities.fields_choices import *


class Activity(models.Model):
    created_by = models.ForeignKey(User)
    magazine = models.ForeignKey(Magazine)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_time = models.DateField(auto_now_add=True)
    start_time = models.DateField()
    dead_time = models.DateField()
    exchange_ddl = models.DateField(auto_now_add=True, blank=True)
    winning_no = models.CharField(max_length=10)
    draw_desc = models.CharField(max_length=200)

    status = models.SmallIntegerField(choices=status_choices)

    class Meta:
        verbose_name = u"活动"
        verbose_name_plural = u"活动"

    def __unicode__(self):
        return self.name


class Publish(models.Model):
    magazine = models.ForeignKey(Magazine)
    activity = models.ForeignKey(Activity)
    winning_no = models.CharField(max_length=10)
    draw_desc = models.CharField(max_length=200)

    class Meta:
        verbose_name = u"公布号码"
        verbose_name_plural = u"公布号码"

    def __unicode__(self):
        return u"活动名称 %s" % self.activity


class Question(models.Model):
    activity = models.ForeignKey(Activity)
    question_text = HTMLField(max_length=1000)
    answer = models.CharField(choices=ans_choices, max_length=2)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)

    class Meta:
        verbose_name = u"题目"
        verbose_name_plural = u"题目"

    def __unicode__(self):
        return u"题目 %s" % self.id


def validate_cell(value):
    if len(value) != 11 and not value.startswith("1"):
        raise ValidationError(u"%s is not valid tell no" % value)


class Report(models.Model):
    user = models.ForeignKey(User)
    cell = models.CharField(max_length=11, validators=[validate_cell])
    level = models.SmallIntegerField(choices=level_choices)
    lucky_no = models.IntegerField()
    accept_time = models.DateField()

    class Meta:
        verbose_name = u"活动报表"
        verbose_name_plural = u"活动报表"
