# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_remove_job_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='contact_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.ContactProfile'),
        ),
    ]
