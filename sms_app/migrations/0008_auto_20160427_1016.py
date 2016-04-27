# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0007_messagetemplate_messagetemplateautoreply_messagetemplatesendhistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagetemplateautoreply',
            name='messagetemplate_ptr',
        ),
        migrations.RemoveField(
            model_name='messagetemplateautoreply',
            name='response_message',
        ),
        migrations.DeleteModel(
            name='MessageTemplateAutoReply',
        ),
    ]
