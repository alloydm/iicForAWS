# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-27 16:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it20', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newidea',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
