# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0021_auto_20160530_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagetemplateusersfilter',
            name='balance_operator',
            field=models.CharField(default=b'', max_length=5, choices=[(b'__lte', b'__lte'), (b'__gte', b'__gte'), (b'', b'')]),
            preserve_default=True,
        ),
    ]
