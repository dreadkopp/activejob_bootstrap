# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 10:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20170626_2253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
    ]
