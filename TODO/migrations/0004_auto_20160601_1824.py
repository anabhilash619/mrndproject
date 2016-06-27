# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 12:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0003_auto_20160601_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='duedate',
            field=models.DateField(default=datetime.datetime(2016, 6, 1, 12, 54, 54, 879000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default=datetime.datetime(2016, 6, 1, 12, 54, 54, 879000, tzinfo=utc)),
        ),
    ]
