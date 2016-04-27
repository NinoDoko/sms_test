# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0002_auto_20160427_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagetemplateautoreply',
            name='response_message',
            field=models.CharField(default='asd', max_length=30),
            preserve_default=False,
        ),
    ]
