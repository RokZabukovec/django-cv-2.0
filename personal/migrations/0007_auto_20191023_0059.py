# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-23 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_project_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tehnologies',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='projectmedia',
            name='is_cover',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='overview',
            field=models.TextField(max_length=200),
        ),
    ]
