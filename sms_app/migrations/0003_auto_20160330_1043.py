# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0002_auto_20160330_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagetemplate',
            name='template_title',
            field=models.CharField(default=b'Sample title', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='messagetemplate',
            name='template_text',
            field=models.CharField(default=b'Sample text', max_length=200),
            preserve_default=True,
        ),
    ]
