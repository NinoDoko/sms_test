# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0007_auto_20160426_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageTemplateAutoReply',
            fields=[
                ('messagetemplate_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='sms_app.MessageTemplate')),
                ('template_type', models.CharField(default=b'template_for_sending', max_length=20, choices=[(b'template_for_sending', b'template_for_sending'), (b'template_auto_reply', b'template_auto_reply')])),
                ('response_message', models.ForeignKey(related_name='automated_reply_to_template', to='sms_app.MessageTemplate')),
            ],
            options={
            },
            bases=('sms_app.messagetemplate',),
        ),
    ]
