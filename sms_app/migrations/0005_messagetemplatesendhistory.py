# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0004_contact_contact_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageTemplateSendHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sent_date', models.DateTimeField()),
                ('message_template', models.ForeignKey(to='sms_app.MessageTemplate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
