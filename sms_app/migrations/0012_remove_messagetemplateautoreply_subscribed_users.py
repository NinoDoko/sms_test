# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0011_messagetemplateautoreply_subscribed_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagetemplateautoreply',
            name='subscribed_users',
        ),
    ]
