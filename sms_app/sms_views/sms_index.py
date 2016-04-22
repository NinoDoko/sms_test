from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sms_app.models import *


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
    
def log_out(request):
    logout(request)
    return redirect('/sms_app')
