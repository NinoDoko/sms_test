import re
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sms_app.models import *


@login_required
def sms_tools_log(request):
    log_file = open('/var/log/smstools/smsd.log', 'r').read()
    all_users = Contact.objects.all()
    regex_failed_send = '(.*), (\w*):[ !]*(Sending SMS to (\d+) failed. User (\w+ \w*) not subscribed.*\.)'
    log_message_errors = [re.search(regex_failed_send, x) for x in log_file.split('\n')]
    print [x.groups() for x in log_message_errors if x]
    log_message_errors = [{'user' : all_users.get(phone_number = x.groups()[3]), 'date' : x.groups()[0], 'device' : x.groups()[1], 'number' : x.groups()[3], 'message' : x.groups()[2]} for x in log_message_errors if x]
    return render(request, 'sms_app/sms_tools_log.html', {'log_message_errors' : log_message_errors})
