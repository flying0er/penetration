# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmaper', '0003_nmapprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='nmapscan',
            name='status_text',
            field=models.CharField(default='waiting', max_length=16),
            preserve_default=False,
        ),
    ]
