# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 01:30
from __future__ import unicode_literals

from django.db import migrations


def add_contact_profiles(apps, schema_editor):
    Ansprechpartner = apps.get_model('ansprechpartner', 'Ansprechpartner')

    for ap in Ansprechpartner.objects.all():
        for contact in ap.contacts.all():
            ap.contact_profiles.add(contact.contactprofile_set.first())


class Migration(migrations.Migration):

    dependencies = [
        ('ansprechpartner', '0003_ansprechpartner_contact_profiles'),
    ]

    operations = [
        migrations.RunPython(add_contact_profiles),
    ]