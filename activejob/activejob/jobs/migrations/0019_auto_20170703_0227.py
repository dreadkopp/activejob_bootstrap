# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 00:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0018_auto_20170702_2320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactprofile',
            options={'ordering': ['contact__last_name', 'contact__first_name']},
        ),
    ]
