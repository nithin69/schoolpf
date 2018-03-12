# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0004_auto_20161227_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='truck_type',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'Loading', b'Loading'), (b'Unloading', b'Unloading'), (b'Unpacking', b'Unpacking')]),
        ),
        migrations.AlterField(
            model_name='truck',
            name='truck_type',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'Loading', b'Loading'), (b'Unloading', b'Unloading'), (b'Unpacking', b'Unpacking')]),
        ),
    ]
