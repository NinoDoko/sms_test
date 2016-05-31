import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sms_app.models import *
from sms_actions import query_users_from_get_args
from sms_app.forms import *

def template_action(request, old_template):
    try:
        if 'edit_filter' in request.POST:
            new_filter = MessageFilterForm(request.POST)
            new_filter.is_valid()
            clean_data = new_filter.clean()
            print clean_data
            new_filter = MessageTemplateUsersFilter(**clean_data)
            new_filter.save()
            return
        if 'crontab' in request.POST:
            crondate = CronDateForm(request.POST).save(commit=False)
            crondate.scheduled_template = old_template
            #todo actually create cronjob
            crondate.save()
        else:
            old_template.template_text = request.POST.get('sms_template')
            old_template.received_text = request.POST.get('received_text')
    except old_template.DoesNotExist as e:
        pass
    old_template.save()



@login_required
def view_sms_template(request, sms_id):
    old_template = MessageTemplate.objects.all().get(pk = sms_id)
    template_is_not_reply = False
    try: 
        old_template = old_template.messagetemplateautoreply
    except old_template.DoesNotExist as e:
        template_is_not_reply = True

    crondate_form = CronDateForm()
    crondate_form.scheduled_template = old_template

    filter_form = MessageFilterForm()

    subscribed_users = []
    users = Contact.objects.all()
    test_contact = users.all().filter(name = 'Test')[0]
    
    
    if request.POST : 
        template_action(request, old_template)

    users = query_users_from_get_args(request, users)
    return render(request, 'sms_app/view_sms_template.html', {'sms_template' : old_template, 'test_contact' : test_contact, 'queried_users' : users, 'template_is_not_reply' : template_is_not_reply, 'cronform' : crondate_form, 'filter_form' : filter_form})
