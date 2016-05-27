import datetime
from django.shortcuts import render, redirect
from sms_app.models import *


def unschedule_template(request, template_id, schedule_id):
    template = MessageTemplate.objects.all().get(pk = template_id)
    cron_schedule = MessageTemplateSchedule.objects.all().get(pk = schedule_id)
    #todo actually remove cronjob
    cron_schedule.delete()
    return redirect("sms_app:view_sms_template", template_id)
