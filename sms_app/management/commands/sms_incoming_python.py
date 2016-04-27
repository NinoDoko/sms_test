from django.core.management.base import BaseCommand, CommandError
from sms_app.models import *

class Command(BaseCommand):
    help = 'Receives sms messages, parses them and returns a response. '

    def handle(self, *args, **options):
        message = open(args[0], 'r').read().split('\n')
        message_from = message[0].split(':')[1].replace(' ', '')
        user_from = Contact.objects.get(phone_number = message_from)
        message = '\n'.join([x for x in message if ':' not in x])
        print 'Message is : ', message, '\nfrom : ', user_from
