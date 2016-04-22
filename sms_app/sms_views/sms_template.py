import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sms_app.models import *
from sms_actions import query_users_from_get_args
    
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

