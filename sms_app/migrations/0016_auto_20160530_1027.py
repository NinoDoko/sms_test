# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0015_messagetemplateschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagetemplateschedule',
            name='day_of_week',
            field=models.CharField(default=b'*', max_length=3, choices=[(b'*', b'*'), (b'Mon', b'Mon'), (b'Tue', b'Tue'), (b'Wed', b'Wed'), (b'Thu', b'Thu'), (b'Fri', b'Fri'), (b'Sat', b'Sat'), (b'Sun', b'Sun')]),
            preserve_default=True,
        ),
    ]
