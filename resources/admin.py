#! /usr/bin/env python
# -*- coding: utf8 -*-

from django.contrib import admin

from resources.models import Magazine


class MagazineAdmin(admin.ModelAdmin):
    exclude = ["created_by"]
    list_display = ["name", "volume", "description"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


admin.site.register(Magazine, MagazineAdmin)
