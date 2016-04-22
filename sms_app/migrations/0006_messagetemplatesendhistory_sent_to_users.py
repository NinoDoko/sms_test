# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0005_messagetemplatesendhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagetemplatesendhistory',
            name='sent_to_users',
            field=models.ManyToManyField(to='sms_app.Contact'),
            preserve_default=True,
        ),
    ]
