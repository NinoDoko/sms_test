# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0027_messagetemplateschedule_monthky'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagetemplateschedule',
            old_name='monthky',
            new_name='monthly',
        ),
    ]
