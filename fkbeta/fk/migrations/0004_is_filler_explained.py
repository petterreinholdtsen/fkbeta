# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-01-01 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fk', '0003_is_filler_explained'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='is_filler',
            field=models.BooleanField(default=False, help_text=b'You still have the editorial responsibility.  Only affect videos from members.', verbose_name=b'Play automatically?'),
        ),
    ]
