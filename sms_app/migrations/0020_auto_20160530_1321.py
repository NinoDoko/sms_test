# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0019_auto_20160530_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='balance',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_last_name',
            field=models.CharField(default=b'', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_name',
            field=models.CharField(default=b'', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default=b'', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(default=b'38975000000', max_length=11),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='messagetemplateusersfilter',
            name='address',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='messagetemplateusersfilter',
            name='balance',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='messagetemplateusersfilter',
            name='contact_last_name',
            field=models.CharField(default=b'', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='messagetemplateusersfilter',
            name='contact_name',
            field=models.CharField(default=b'', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='messagetemplateusersfilter',
            name='name',
            field=models.CharField(default=b'', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='messagetemplateusersfilter',
            name='phone_number',
            field=models.CharField(default=b'38975000000', max_length=11),
            preserve_default=True,
        ),
    ]
