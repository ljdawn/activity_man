#! /usr/bin/env python
# -*- coding: utf8 -*-
import logging

from django.contrib.auth.decorators import login_required

from activities.models import Activity
from resources.models import Magazine
from xyyedu_admin.utils import api_required, json_response


logger = logging.getLogger(__name__)


# @api_required
def get_activity_info(request, activity_id=1):
    data = {"code": "err"}
    try:
        activity = Activity.objects.get(pk=activity_id)
    except Activity.DoesNotExist:
        data.update({"code": "err", "desc": u"请输入正确的活动id"})
        return json_response(data)
    data.update({
        "code": "ok",
        "act_info": {
            "act_id": activity.id,
            "act_name": activity.name,
            "act_info": activity.description,
            "question": list(activity.question_set.all().values_list("id", flat=True))
        }
    })
    return json_response(data)


@login_required
def get_mag_activities(request, magazine_id=1):
    data = {"code": "err"}
    try:
        magazine = Magazine.objects.get(pk=magazine_id)
    except Magazine.DoesNotExist:
        data.update({"code": "err", "desc": u"请输入正确的杂志id"})
        return json_response(data)
    activities = Activity.objects.filter(magazine=magazine).all().values_list("id", "name")
    data.update({
        "code": "ok",
        "activities": list(activities)
    })

    return json_response(data)