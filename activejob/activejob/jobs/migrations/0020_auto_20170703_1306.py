# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 11:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0019_auto_20170703_0227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactprofile',
            options={'ordering': ['contact__last_name', 'contact__first_name', 'pk']},
        ),
    ]
