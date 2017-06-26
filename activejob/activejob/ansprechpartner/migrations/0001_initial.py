# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0003_auto_20170519_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ansprechpartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('field', models.CharField(max_length=100)),
                ('banner_color', models.CharField(max_length=6)),
                ('banner_slogan', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('contacts', models.ManyToManyField(to='jobs.Contact')),
            ],
        ),
    ]