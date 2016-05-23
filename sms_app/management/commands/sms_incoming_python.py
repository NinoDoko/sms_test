from django.core.management.base import BaseCommand, CommandError
from sms_app.models import *
from sms_app.sms_views.sms_actions import smstools_send_messages

class Command(BaseCommand):
    help = 'Receives sms messages, parses them and returns a response. '

    def handle(self, *args, **options):
        message = open(args[0], 'r').read().split('\n')
        message_from = message[0].split(':')[1].replace(' ', '')
        try:
            user_from = Contact.objects.get(phone_number = message_from)
        except Exception as e: 
            print 'Received message from unknown user; phone number is : ', message_from
            
        message = ''.join([x for x in message if ':' not in x])

        try:
            response_template = MessageTemplateAutoReply.objects.all().get(received_text=message)
        except Exception as e: 
            print 'Received faulty message : ', message
        
        if user_from not in response_template.subscribed_users.all():
            print 'Sending SMS to', user_from.phone_number, 'failed. User', user_from.contact_name, user_from.contact_last_name,'not subscribed; message sent was :', message,'.'
            return
        
        if not response_template: 
            template = MessageTemplate.objects.all().get(template_title='help_template')
        else: 
            template = MessageTemplate.objects.get(pk = response_template.pk)
            
        smstools_send_messages(template, [user_from])
