from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from sms_app.models import *


@login_required
def sms_template_index(request):
    users = Contact.objects.all()
    test_contact = users.all().get(name = 'Test')
    if request.POST : 
        if request.POST.get('view_received_text'):
            new_template = MessageTemplateAutoReply(template_text = request.POST['sms_template'], template_title = request.POST['template_title'], received_text = request.POST['received_text'])
        else:
            new_template = MessageTemplate(template_text = request.POST['sms_template'], template_title = request.POST['template_title'])
        if new_template.save():
            messages.success(request, 'Template saved successfuly')
    auto_replies = MessageTemplateAutoReply.objects.all()
    sms_templates = MessageTemplate.objects.all()
    return render(request, 'sms_app/sms_template_index.html', {'sms_templates' : sms_templates, 'auto_replies' : auto_replies, 'test_contact' : test_contact})
    
def log_out(request):
    logout(request)
    return redirect('/sms_app')
