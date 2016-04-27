from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from sms_app.models import *


@login_required
def sms_template_index(request):
    users = Contact.objects.all()
    test_contact = users.all().filter(name = 'Test')[0]
    if request.POST : 
        if request.POST['view_received_text']:
            new_template = MessageTemplateAutoReply(template_text = request.POST['sms_template'], template_title = request.POST['template_title'], received_text = request.POST['received_text'])
        else:
            new_template = MessageTemplate(template_text = request.POST['sms_template'], template_title = request.POST['template_title'])
        if new_template.save():
            messages.success(request, 'Template saved successfuly')
    auto_replies = MessageTemplateAutoReply.objects.all()
    sms_templates = [x for x in MessageTemplate.objects.all() if x.pk not in [y.pk for y in auto_replies]]
    return render(request, 'sms_app/sms_template_index.html', {'sms_templates' : sms_templates, 'auto_replies' : auto_replies, 'test_contact' : test_contact})
    
def log_out(request):
    logout(request)
    return redirect('/sms_app')
