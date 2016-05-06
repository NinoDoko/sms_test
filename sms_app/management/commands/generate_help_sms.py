from django.core.management.base import BaseCommand, CommandError
from sms_app.models import *
from sms_app.sms_views.sms_actions import smstools_send_messages

class Command(BaseCommand):
    help = 'Generates a help message containing all actions that can be received as text.'

    def handle(self, *args, **options):
        auto_replies = [x.received_text for x in MessageTemplateAutoReply.objects.all()] 
        if 'one_line' in args: 
            help_message = 'Available actions : ' + ', '.join(auto_replies)
        else: 
            help_message = 'Available actions : \n' + '\n'.join([x + ':' for x in auto_replies])
        if 'create_object' in args: 
            try: 
                help_template = MessageTemplateAutoReply.objects.get(template_title = 'help_template')
            except Exception: 
                help_template = MessageTemplateAutoReply(template_title = 'help_template')
            help_template.template_text = help_message
            help_template.save()
        return help_message
