# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-28 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0008_auto_20191023_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmedia',
            name='image',
            field=models.ImageField(blank=True, upload_to='img/'),
        ),
    ]
