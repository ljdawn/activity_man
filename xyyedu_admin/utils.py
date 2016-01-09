#! /usr/bin/env python
# -*- coding: utf8 -*-

import json
import base64


from functools import wraps

from django.conf import settings
from django.utils import translation
from django.http import HttpResponse


class AdminLocaleURLMiddleware(object):
    def process_request(self, request):
        if request.path.startswith('/admin'):
            request.LANG = getattr(settings, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)
            translation.activate(request.LANG)
            request.LANGUAGE_CODE = request.LANG


def json_response(data):
    return HttpResponse(json.dumps(data), content_type='application/json')


def api_required(view_func):
    @wraps
    def check_token(request, *args, **kwargs):
        """check the token to verify client"""
        signature = request.META.get("HTTP_TOKEN", "")
        signature = base64.b64decode(signature)
        if signature:
            return view_func(request, *args, **kwargs)
        else:
            return json_response({"status": "error", "description": "wrong token"})
    return check_token