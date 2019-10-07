# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-07 09:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_auto_20191007_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='school',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sms.School'),
            preserve_default=False,
        ),
    ]
