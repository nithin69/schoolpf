# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0002_load_truck'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('phone1', models.CharField(max_length=200, null=True, blank=True)),
                ('phone2', models.CharField(max_length=200, null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('aadhar_card', models.CharField(max_length=16)),
                ('vehicle_no', models.CharField(max_length=10, null=True, blank=True)),
                ('vehicle_type', models.CharField(max_length=200, null=True, blank=True)),
                ('attach_files', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('driving_license', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Enrollment',
            },
        ),
    ]
