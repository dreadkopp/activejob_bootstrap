# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referenzen', '0004_auto_20170629_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]