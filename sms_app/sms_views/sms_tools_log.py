import re
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sms_app.models import *


@login_required
def sms_tools_log(request):
    log_file = open('/var/log/smstools/smsd.log', 'r').read()
    all_users = Contact.objects.all()
    log_message_errors = [re.search('(.*), (.*): Sending SMS to (\d+) failed, trying time (\d+) sec\. Retries: (\d+)\.', x) for x in log_file.split('\n')]
    log_message_errors = [{'user' : all_users.filter(phone_number = x.groups()[2])[0], 'date' : x.groups()[0], 'device' : x.groups()[1], 'number' : x.groups()[2], 'trying_time' : x.groups()[3], 'retries' : x.groups()[4], 'message' : x.group(0)} for x in log_message_errors if x]
    return render(request, 'sms_app/sms_tools_log.html', {'log_message_errors' : log_message_errors})
