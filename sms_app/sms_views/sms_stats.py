from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sms_app.models import *


@login_required
def sms_stats(request, history_no):
    sms_history = MessageTemplateSendHistory.objects.all().filter(pk = history_no)[0]
    return render(request, 'sms_app/message_sent_stats.html', {'sms_history' : sms_history})
