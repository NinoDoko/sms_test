from django.db import models

class Contact(models.Model):
    contact_type_choices = [('business', 'business'), ('private', 'private')]
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    contact_name = models.CharField(max_length = 30)
    contact_last_name = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 11)
    contact_type = models.CharField(max_length = 10, choices = contact_type_choices, default = 'private')
    balance = models.IntegerField()
    
    def __unicode__(self):
        return self.name
        
    #This exists for easier attribute parsing. 
    #Used in the new_template_form template, where the model attributes are substituted into a test form using jquery. 
    def attrs(self):
        for attr, value in self.__dict__.iteritems():
            yield attr, value
        
class MessageTemplate(models.Model):
    template_title = models.CharField(max_length = 30, default = 'Sample title')
    template_text = models.CharField(max_length = 200, default = 'Sample text')
    
    def __unicode__(self):
        return self.template_title
        
class MessageTemplateAutoReply(MessageTemplate):
    template_type_choices = [('template_for_sending', 'template_for_sending'), ('template_auto_reply', 'template_auto_reply')]
    template_type = models.CharField(max_length = 20, choices = template_type_choices, default = 'template_for_sending')
    response_message = models.ForeignKey('MessageTemplate', related_name = 'automated_reply_to_template')
    
class MessageTemplateSendHistory(models.Model):
    message_template = models.ForeignKey('MessageTemplate')
    sent_to_users = models.ManyToManyField(Contact)
    sent_date = models.DateTimeField()
