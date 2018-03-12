# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_id', models.CharField(max_length=200, null=True, blank=True)),
                ('from_location', models.CharField(max_length=200, null=True, blank=True)),
                ('to_location', models.CharField(max_length=200, null=True, blank=True)),
                ('capacity', models.CharField(max_length=200, null=True, blank=True)),
                ('scheduled_date', models.DateField(null=True, blank=True)),
                ('posted_by', models.CharField(max_length=200, null=True, blank=True)),
                ('truck_type', models.CharField(max_length=200, null=True, blank=True)),
                ('distance', models.CharField(max_length=200, null=True, blank=True)),
                ('approx_travelling_time', models.CharField(max_length=200, null=True, blank=True)),
                ('truck_image', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Load Details',
            },
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_id', models.CharField(max_length=200, null=True, blank=True)),
                ('from_location', models.CharField(max_length=200, null=True, blank=True)),
                ('to_location', models.CharField(max_length=200, null=True, blank=True)),
                ('capacity', models.CharField(max_length=200, null=True, blank=True)),
                ('scheduled_date', models.DateField(null=True, blank=True)),
                ('posted_by', models.CharField(max_length=200, null=True, blank=True)),
                ('truck_type', models.CharField(max_length=200, null=True, blank=True)),
                ('distance', models.CharField(max_length=200, null=True, blank=True)),
                ('approx_travelling_time', models.CharField(max_length=200, null=True, blank=True)),
                ('truck_image', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Truck Details',
            },
        ),
    ]
