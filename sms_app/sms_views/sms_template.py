import datetime
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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

def log_out(request):
    logout(request)
    return redirect('/sms_app')
    
@login_required
def sms_template_index(request):
    users = Contact.objects.all()
    test_contact = users.all().filter(name = 'Test')[0]
    if request.POST : 
        new_template = MessageTemplate(template_text = request.POST['sms_template'], template_title = request.POST['template_title'])
        if new_template.save():
            messages.success(request, 'Template saved successfuly')
    sms_templates = MessageTemplate.objects.all()
    return render(request, 'sms_app/sms_template_index.html', {'sms_templates' : sms_templates, 'test_contact' : test_contact})

@login_required
def view_sms_template(request, sms_id):
    old_template = MessageTemplate.objects.all().filter(pk = sms_id)[0]
    users = Contact.objects.all()
    test_contact = users.all().filter(name = 'Test')[0]
    if request.POST : 
        old_template.template_text = request.POST.get('sms_template')
        old_template.save()
    users = query_users_from_get_args(request, users)
    return render(request, 'sms_app/view_sms_template.html', {'sms_template' : old_template, 'test_contact' : test_contact, 'queried_users' : users})
    
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
    print '\n'.join(['Texting ' + x.name + ' with phone number ' + x.phone_number + ' with message : ' + replace_tags(template, x) for x in users])
    sent_template = MessageTemplateSendHistory(message_template = template, sent_date = datetime.datetime.now(), )
    sent_template.save()
    return redirect('sms_app:sms_template_index')
