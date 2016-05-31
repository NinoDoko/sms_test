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
        
class MessageFilterForm(ModelForm):
    def validate(self):
        validated = super(MessageFilterForm, self).validate()
        print validated, 'is validted'
        return True
        
    def is_valid(self):
        validated = super(MessageFilterForm, self).is_valid()
        return True
        
    def clean(self):
        cleaned_data = super(MessageFilterForm, self).clean()
        print 'Cleaned is : ', cleaned_data
        default_values = {'name':'', 'contact_name':'', 'contact_last_name':'', 'address':'', 'balance':0, 'phone_number':'', 'balance_operator':''}
        for key in default_values:
            if key not in cleaned_data:
                cleaned_data[key] = default_values[key]
        
        return cleaned_data
        
    class Meta:
        model = MessageTemplateUsersFilter
        exclude = ['filter_for_schedule']
