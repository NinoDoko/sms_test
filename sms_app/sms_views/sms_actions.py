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
    
    smstools_send_messages(template, users)

    sent_template = MessageTemplateSendHistory(message_template = template, sent_date = datetime.datetime.now())
    sent_template.save()
    sent_template.sent_to_users.add(*users)
    return redirect('sms_app:sms_template_index')


def add_auto_reply(request, sms_id):
    return manage_auto_reply(request, 'add', sms_id)

def remove_auto_reply(request, sms_id):
    return manage_auto_reply(request, 'remove', sms_id)

def manage_auto_reply(request, action, sms_id):
    if action == 'add':
        old_template = MessageTemplate.objects.get(pk = sms_id)
        new_template = MessageTemplateAutoReply.create_from_template(old_template, '')
        old_template.delete()
        new_template.save()
        return redirect('sms_app:view_sms_template', new_template.pk )
    elif action == 'remove':
        old_template = MessageTemplateAutoReply.objects.get(pk = sms_id)
        new_template = MessageTemplate.create_from_reply(old_template)
        old_template.delete()
        new_template.save()
        return redirect('sms_app:sms_template_index')
    else: raise Exception('Unknown action : ', action)    
    
    
def smstools_send_messages(template, users):
    messages = [(x.phone_number, replace_tags(template, x)) for x in users] 
    for message in messages: 
        command = ['sendsms', message[0], message[1]]
        print 'Message : ', subprocess.list2cmdline(command)
#        s = subprocess.call(command)
#        print 'Sent message ', message, ' received : ', s

