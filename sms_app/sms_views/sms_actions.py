import datetime, subprocess
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from sms_app.models import *

def query_users_from_get_args(request, users):
    if request.GET :
        if request.GET.get('name'):
            users = users.filter(name__icontains = request.GET['name'])
        if request.GET.get('address'):
            users = users.filter(address__icontains = request.GET['address'])
        if request.GET.get('balance'):
            #The next line is why I love python
            users = users.filter(**{'balance__' + request.GET.get('balance_operator') : request.GET['balance']})
        if request.GET.get('contact_type'):
            users = users.filter(contact_type = request.GET['contact_type'])    
    return users


def replace_tags(template, user):
    tags = ['<name>', '<balance>', '<contact_type>', '<phone_number>', '<address>', '<contact_name>', '<contact_last_name>']
    text = template.template_text
    for tag in tags:
        text = text.replace(tag, str(getattr(user, tag[1:-1])))
    return text

def delete_sms_template(request, sms_id):
    template = MessageTemplate.objects.all().filter(pk = sms_id)[0]
    template.delete()
    return redirect('sms_app:sms_template_index')

@login_required
def send_sms(request, sms_id):
    users = []
    users = [user for user in Contact.objects.all() if user.name in request.POST]
    users = query_users_from_get_args(request, users)
    template = MessageTemplate.objects.all().filter(pk = sms_id)[0]
    messages = [(x.phone_number, replace_tags(template, x)) for x in users] 
    for message in messages: 
        command = ['sendsms', message[0], message[1]]
        print 'Message : ', subprocess.list2cmdline(command)
        s = subprocess.call(command)
#        print 'Sent message ', message, ' received : ', s

    sent_template = MessageTemplateSendHistory(message_template = template, sent_date = datetime.datetime.now())
    sent_template.save()
    sent_template.sent_to_users.add(*users)
    return redirect('sms_app:sms_template_index')