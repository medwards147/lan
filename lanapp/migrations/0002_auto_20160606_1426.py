# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import lanapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('lanapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-event_start_date',)},
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_date',
            field=models.DateTimeField(verbose_name='Event End'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_date',
            field=models.DateTimeField(verbose_name='Event Start'),
        ),
        migrations.RemoveField(
            model_name='event',
            name='games',
        ),
        migrations.AddField(
            model_name='event',
            name='games',
            field=models.ManyToManyField(blank=True, to='lanapp.Game'),
        ),
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', help_text='Image field for game', null=True, upload_to=lanapp.models.upload_location, width_field='width_field'),
        ),
    ]
