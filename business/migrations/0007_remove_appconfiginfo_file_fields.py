# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-12 08:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_remove_businessaccountinfo_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appconfiginfo',
            name='file_fields',
        ),
    ]
