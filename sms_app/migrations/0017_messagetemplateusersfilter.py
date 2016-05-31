# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0016_auto_20160530_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageTemplateUsersFilter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('contact_name', models.CharField(max_length=30)),
                ('contact_last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=11)),
                ('contact_type', models.CharField(default=b'private', max_length=10, choices=[(b'business', b'business'), (b'private', b'private')])),
                ('balance', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
