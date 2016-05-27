import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sms_app.models import *
from sms_actions import query_users_from_get_args
from sms_app.forms import *

@login_required
def view_sms_template(request, sms_id):
    old_template = MessageTemplate.objects.all().get(pk = sms_id)
    template_is_not_reply = False
    try: 
        old_template = old_template.messagetemplateautoreply
    except old_template.DoesNotExist as e:
        template_is_not_reply = True
        pass

    crondate_form = CronDateForm()

    subscribed_users = []
    users = Contact.objects.all()
    test_contact = users.all().filter(name = 'Test')[0]
    if request.POST : 
        if not template_is_not_reply:
            old_template.received_text = request.POST.get('received_text')
        old_template.template_text = request.POST.get('sms_template')
        old_template.save()
    users = query_users_from_get_args(request, users)
    return render(request, 'sms_app/view_sms_template.html', {'sms_template' : old_template, 'test_contact' : test_contact, 'queried_users' : users, 'template_is_not_reply' : template_is_not_reply, 'cronform' : crondate_form})
