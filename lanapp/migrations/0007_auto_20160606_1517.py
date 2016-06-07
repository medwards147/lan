# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lanapp', '0006_auto_20160606_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='games',
        ),
        migrations.RemoveField(
            model_name='event',
            name='sponsors',
        ),
        migrations.RemoveField(
            model_name='game',
            name='gaming_system',
        ),
        migrations.AddField(
            model_name='game',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lanapp.Event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sponsor',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lanapp.Event'),
            preserve_default=False,
        ),
    ]