# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-03 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it20', '0004_newidea_upi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newidea',
            name='UPI',
            field=models.CharField(default='Your Transaction ID with anju.marina.lobo@oksbi HERE', max_length=100),
        ),
    ]
