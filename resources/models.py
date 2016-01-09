#! /usr/bin/env python
# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User


class Magazine(models.Model):
    created_by = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=6)
    volume = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = u"杂志"
        verbose_name_plural = u"杂志"

    def __unicode__(self):
        return self.name
