from django.core.management.base import BaseCommand, CommandError
from sms_app.models import *
from sms_app.sms_views.sms_actions import smstools_send_messages, query_users_from_dict

class Command(BaseCommand):
    help = "Receives a schedule object's pk, filters the users based on the filter of the schedule (if it exists) and sends messages. "

    def handle(self, *args, **options):
        schedule_pk = args[0]
        
        schedule = MessageTemplateSchedule.objects.all().get(pk = schedule_pk)
        schedule_filter = schedule.messagetemplateusersfilter
        all_users = Contact.objects.all()
        template = schedule.scheduled_template
        
        try:
            filtered_users = query_users_from_dict(schedule_filter.__dict__, all_users)
        except Exception as e:
            print e, schedule_filter.__dict__
            filtered_users = all_users
        
        smstools_send_messages(template, filtered_users)
