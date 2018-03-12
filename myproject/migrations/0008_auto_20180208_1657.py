# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0007_auto_20180208_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fm16',
            old_name='f_bank',
            new_name='bank_no',
        ),
        migrations.RenameField(
            model_name='fm16',
            old_name='f_dept',
            new_name='designation',
        ),
        migrations.RenameField(
            model_name='fm16',
            old_name='f_designation',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='fm16',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='fm16',
            old_name='f_pan',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='fm16',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fm16',
            name='office_address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fm16',
            name='pan',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fm16',
            name='phone',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
