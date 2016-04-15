from django.contrib import admin
from django.db import models

class Contact(models.Model):
    contact_type_choices = [('business', 'business'), ('private', 'private')]
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    contact_name = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 10)
    contact_type = models.CharField(max_length = 10, choices = contact_type_choices, default = 'private')
    balance = models.IntegerField()
    
    def __unicode__(self):
        return self.name
        
class MessageTemplate(models.Model):
    template_title = models.CharField(max_length = 30, default = 'Sample title')
    template_text = models.CharField(max_length = 200, default = 'Sample text')
    
    def __unicode__(self):
        return self.template_title
    
    
admin.site.register(Contact)
admin.site.register(MessageTemplate)
# Create your models here.
