from django.core.management.base import BaseCommand, CommandError
from sms_app.models import *
from sms_app.sms_views.sms_actions import smstools_send_messages

class Command(BaseCommand):
    help = 'Receives sms messages, parses them and returns a response. '

    def handle(self, *args, **options):
        message = open(args[0], 'r').read().split('\n')
        message_from = message[0].split(':')[1].replace(' ', '')
        user_from = Contact.objects.get(phone_number = message_from)
        message = ''.join([x for x in message if ':' not in x])

        response_template = MessageTemplateAutoReply.objects.all().get(received_text=message)
        
        if user_from not in response_template.subscribed_users.all():
            print 'User not subscribed'
            return
        
        if not response_template: 
            template = MessageTemplate.objects.all().get(template_title='help_template')
        else: 
            template = MessageTemplate.objects.get(pk = response_template.pk)
            
        smstools_send_messages(template, [user_from])
