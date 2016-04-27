# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0006_auto_20160427_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template_title', models.CharField(default=b'Sample title', max_length=30)),
                ('template_text', models.CharField(default=b'Sample text', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MessageTemplateAutoReply',
            fields=[
                ('messagetemplate_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='sms_app.MessageTemplate')),
                ('response_message', models.ForeignKey(related_name='automated_reply_to_template', to='sms_app.MessageTemplate')),
            ],
            options={
            },
            bases=('sms_app.messagetemplate',),
        ),
        migrations.CreateModel(
            name='MessageTemplateSendHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sent_date', models.DateTimeField()),
                ('message_template', models.ForeignKey(to='sms_app.MessageTemplate')),
                ('sent_to_users', models.ManyToManyField(to='sms_app.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
