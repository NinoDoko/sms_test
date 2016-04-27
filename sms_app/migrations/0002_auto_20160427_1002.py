# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagetemplateautoreply',
            name='response_message',
            field=models.ForeignKey(related_name='automated_reply_to_template', blank=True, to='sms_app.MessageTemplate', null=True),
            preserve_default=True,
        ),
    ]
