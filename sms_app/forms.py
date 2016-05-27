from django.forms import ModelForm
from sms_app.models import *

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
class CronDateForm(ModelForm):
    class Meta:
        model = MessageTemplateSchedule
        exclude = ['scheduled_template']
