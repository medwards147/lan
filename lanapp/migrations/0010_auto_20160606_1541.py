# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 19:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lanapp', '0009_auto_20160606_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='event_description',
        ),
    ]
