# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=200, null=True, blank=True)),
                ('lastname', models.CharField(max_length=200, null=True, blank=True)),
                ('email', models.CharField(max_length=200, null=True, blank=True)),
                ('phone', models.CharField(max_length=200, null=True, blank=True)),
                ('subject', models.CharField(max_length=200, null=True, blank=True)),
                ('message', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
    ]
