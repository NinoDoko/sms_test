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
    
    @classmethod
    def create_from_reply(cls, auto_reply):
        new_message = cls(template_title = auto_reply.template_title, template_text = auto_reply.template_text)
        return new_message
        
    def __unicode__(self):
        return self.template_title
        

class MessageTemplateAutoReply(MessageTemplate):
    received_text = models.CharField(max_length = 200, default = 'Sample text')
    
    @classmethod
    def create_from_template(cls, template, received_text):
        new_message = cls(template_title = template.template_title, template_text = template.template_text, received_text = received_text)
        return new_message
            
class MessageTemplateSendHistory(models.Model):
    message_template = models.ForeignKey('MessageTemplate')
    sent_to_users = models.ManyToManyField(Contact)
    sent_date = models.DateTimeField()
