# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(default='CNY LAN', max_length=100)),
                ('event_start_date', models.DateTimeField(verbose_name='Event Start')),
                ('event_end_date', models.DateTimeField(verbose_name='Event End')),
                ('pay_button_text', models.CharField(default='Pay here with Paypal', max_length=100)),
                ('venue', models.CharField(blank=True, max_length=75, null=True)),
                ('price', models.IntegerField(blank=True, default=35, null=True)),
                ('street_address', models.CharField(blank=True, max_length=75, null=True)),
                ('city', models.CharField(default='Rome', max_length=75)),
                ('state', models.CharField(default='New York', max_length=75)),
                ('zip_code', models.CharField(default='13440', max_length=75)),
            ],
            options={
                'ordering': ('-event_start_date',),
            },
        ),
    ]