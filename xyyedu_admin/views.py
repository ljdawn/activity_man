#! /usr/bin/env python
# -*- coding: utf8 -*-

from django.shortcuts import render


def render_404(request, *args, **kwargs):
    return render(request, "index.html")