# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 11:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('duedate', models.DateField(default=datetime.date(2016, 6, 1))),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateField(default=datetime.date(2016, 6, 1))),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TODO.TodoItem')),
            ],
        ),
    ]
