# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referenzen', '0002_auto_20170627_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='field',
            new_name='fields',
        ),
    ]
