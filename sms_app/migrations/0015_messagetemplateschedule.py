# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0014_auto_20160523_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageTemplateSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('minute', models.CharField(default=b'*', max_length=2)),
                ('hour', models.CharField(default=b'*', max_length=2)),
                ('day_of_month', models.CharField(default=b'*', max_length=2)),
                ('day_of_week', models.CharField(default=b'*', max_length=3, choices=[(0, b'*'), (1, b'Mon'), (2, b'Tue'), (3, b'Wed'), (4, b'Thu'), (5, b'Fri'), (6, b'Sat'), (7, b'Sun')])),
                ('scheduled_template', models.ForeignKey(to='sms_app.MessageTemplate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
