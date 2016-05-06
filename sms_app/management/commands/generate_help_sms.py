from django.core.management.base import BaseCommand, CommandError
from sms_app.models import *
from sms_app.sms_views.sms_actions import smstools_send_messages

class Command(BaseCommand):
    help = 'Generates a help message containing all actions that can be received as text.'

    def handle(self, *args, **options):
        auto_replies = [x.received_text for x in MessageTemplateAutoReply.objects.all()]
        if args: 
            if args[0] == 'one_line': 
                help_message = 'Available actions : ' + ', '.join(auto_replies)                
        else: 
            help_message = 'Available actions : \n' + '\n'.join([x + ':' for x in auto_replies])
        return help_message
