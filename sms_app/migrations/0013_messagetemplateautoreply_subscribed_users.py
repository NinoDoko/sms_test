# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0012_remove_messagetemplateautoreply_subscribed_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagetemplateautoreply',
            name='subscribed_users',
            field=models.ManyToManyField(to='sms_app.Contact', blank=True),
            preserve_default=True,
        ),
    ]
