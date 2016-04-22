from django.shortcuts import render
from sms_app.models import *

def sms_history(request):
    sms_history = MessageTemplateSendHistory.objects.order_by('-sent_date')
    return render(request, 'sms_app/sms_template_history.html', {'sms_history' : sms_history})
