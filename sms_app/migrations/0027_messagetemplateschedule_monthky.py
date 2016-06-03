# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0026_auto_20160531_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagetemplateschedule',
            name='monthky',
            field=models.CharField(default=b'*', max_length=3, choices=[(b'*', b'*'), (b'Jan', b'Jan'), (b'Feb', b'Feb'), (b'Mar', b'Mar'), (b'Apr', b'Apr'), (b'Jun', b'Jun'), (b'Jul', b'Jul'), (b'Aug', b'Aug'), (b'Sep', b'Sep'), (b'Oct', b'Oct'), (b'Nov', b'Nov'), (b'Dec', b'Dec')]),
            preserve_default=True,
        ),
    ]
