# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0009_messagetemplateautoreply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagetemplateautoreply',
            old_name='response_message',
            new_name='received_text',
        ),
    ]
