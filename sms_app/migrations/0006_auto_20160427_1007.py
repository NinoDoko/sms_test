# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0005_auto_20160427_1006'),
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
        migrations.RemoveField(
            model_name='messagetemplatesendhistory',
            name='message_template',
        ),
        migrations.DeleteModel(
            name='MessageTemplateAutoReply',
        ),
        migrations.DeleteModel(
            name='MessageTemplate',
        ),
        migrations.RemoveField(
            model_name='messagetemplatesendhistory',
            name='sent_to_users',
        ),
        migrations.DeleteModel(
            name='MessageTemplateSendHistory',
        ),
    ]
