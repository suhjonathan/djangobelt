# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-27 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='description',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='travel_end',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='travel_start',
        ),
    ]
