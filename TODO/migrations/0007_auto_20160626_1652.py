# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 11:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0006_auto_20160607_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='created',
            field=models.DateField(default=datetime.datetime(2016, 6, 26, 11, 22, 35, 236000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='duedate',
            field=models.DateField(default=datetime.datetime(2016, 6, 26, 11, 22, 35, 236000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default=datetime.datetime(2016, 6, 26, 11, 22, 35, 235000, tzinfo=utc)),
        ),
    ]