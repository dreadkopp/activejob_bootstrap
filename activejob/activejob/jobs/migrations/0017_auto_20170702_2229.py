# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 20:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_company_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name', 'pk'], 'verbose_name_plural': 'companies'},
        ),
    ]
