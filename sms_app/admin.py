from django.contrib import admin

from .models import *

admin.site.register(Contact)
admin.site.register(MessageTemplate)
admin.site.register(MessageTemplateAutoReply)

# Register your models here.
