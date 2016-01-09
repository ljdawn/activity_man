#! /usr/bin/env python
# -*- coding: utf8 -*-

from django import forms
from django.contrib import admin
from django.conf import settings

from activities.models import Question, Activity, Publish


class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Question
        fields = ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'answer']


class QuestionInline(admin.StackedInline):
    # form = QuestionForm
    fields = ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'answer']
    model = Question
    extra = 1


class ActivityAdmin(admin.ModelAdmin):
    fields = ("magazine", "name", "description", ("start_time", "dead_time"), "status")
    exclude = ["created_by"]
    inlines = [QuestionInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


class PublishAdmin(admin.ModelAdmin):

    class Media:
        js = ("js/jquery-1.11.3.min.js",
              "js/mag_activities.js",)


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Publish, PublishAdmin)
