import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from sms_app.models import *
from sms_actions import query_users_from_dict
from sms_app.forms import *


def create_cronjob(crondate, script_path = ''):
    if not script_path: script_path = settings.BASE_DIR

    crontab_command = 'cd ' + script_path  + '; ./send_filtered_messages.sh ' + str(crondate.pk)
    crontab_dates = crondate.minute + ' ' + crondate.hour + ' ' + crondate.day_of_month + ' ' + crondate.monthly + ' ' + crondate.day_of_week
    open('/etc/cron.d/vapour_sms_schedule_' + str(crondate.pk), 'w').write(crontab_dates + ' root ' + crontab_command + '\n')

def template_action(request, old_template):
    try:
        if 'edit_filter' in request.POST:
            new_filter = MessageFilterForm(request.POST)
            new_filter.is_valid()
            clean_data = new_filter.clean()

            new_filter = MessageTemplateUsersFilter(**clean_data)
            new_filter.balance_operator = request.POST['balance_operator']
            schedule = MessageTemplateSchedule.objects.all().get(pk = request.POST['schedule_id'])
            
            schedule.messagetemplateusersfilter.delete()
            schedule.messagetemplateusersfilter = new_filter

            new_filter.save()
            return
            
        if 'crontab' in request.POST:
            crondate = CronDateForm(request.POST).save(commit=False)
            crondate.scheduled_template = old_template
            #todo actually create cronjob
            crondate.save()
            create_cronjob(crondate)
            new_filter = MessageTemplateUsersFilter(balance = 0, filter_for_schedule = crondate)
            new_filter.save()
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
        if 'users_query' in request.POST:
            print request.POST
            users = query_users_from_dict(request.POST, users)
        else:
            template_action(request, old_template)
    return render(request, 'sms_app/view_sms_template.html', {'sms_template' : old_template, 'test_contact' : test_contact, 'queried_users' : users, 'template_is_not_reply' : template_is_not_reply, 'cronform' : crondate_form, 'filter_form' : filter_form})
