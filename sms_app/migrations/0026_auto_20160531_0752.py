# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0025_auto_20160530_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagetemplateusersfilter',
            name='filter_for_schedule',
            field=models.OneToOneField(null=True, default=None, to='sms_app.MessageTemplateSchedule'),
            preserve_default=True,
        ),
    ]
