# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0008_auto_20160427_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageTemplateAutoReply',
            fields=[
                ('messagetemplate_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='sms_app.MessageTemplate')),
                ('response_message', models.CharField(default=b'Sample text', max_length=200)),
            ],
            options={
            },
            bases=('sms_app.messagetemplate',),
        ),
    ]
