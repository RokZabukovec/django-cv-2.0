# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-28 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0010_auto_20191028_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='overview',
            field=models.TextField(max_length=9999),
        ),
    ]
