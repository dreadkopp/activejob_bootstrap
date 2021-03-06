# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactmessages', '0002_personalanfrage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalanfrage',
            old_name='qualitications',
            new_name='qualifications',
        ),
        migrations.AddField(
            model_name='personalanfrage',
            name='from_date',
            field=models.CharField(default='', max_length=32, verbose_name='Einsatzbeginn'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personalanfrage',
            name='city',
            field=models.CharField(max_length=64, verbose_name='PLZ/Ort*'),
        ),
        migrations.AlterField(
            model_name='personalanfrage',
            name='company',
            field=models.CharField(blank=True, max_length=64, verbose_name='Firma*'),
        ),
        migrations.AlterField(
            model_name='personalanfrage',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-Mail*'),
        ),
        migrations.AlterField(
            model_name='personalanfrage',
            name='first_name',
            field=models.CharField(max_length=64, verbose_name='Vorname*'),
        ),
        migrations.AlterField(
            model_name='personalanfrage',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Name*'),
        ),
        migrations.AlterField(
            model_name='personalanfrage',
            name='phone',
            field=models.CharField(max_length=64, verbose_name='Telefon*'),
        ),
        migrations.AlterField(
            model_name='personalanfrage',
            name='street',
            field=models.CharField(max_length=64, verbose_name='Straße/Hausnummer*'),
        ),
    ]
