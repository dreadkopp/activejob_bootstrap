# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_merge_20170701_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]