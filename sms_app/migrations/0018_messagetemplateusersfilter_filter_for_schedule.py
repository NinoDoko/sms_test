# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0017_messagetemplateusersfilter'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagetemplateusersfilter',
            name='filter_for_schedule',
            field=models.ForeignKey(default=None, to='sms_app.MessageTemplateSchedule'),
            preserve_default=True,
        ),
    ]
