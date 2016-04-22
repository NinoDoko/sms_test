# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0003_auto_20160330_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_last_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
