# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0006_fm16'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fm16',
            options={},
        ),
        migrations.RemoveField(
            model_name='fm16',
            name='truck_image',
        ),
        migrations.AddField(
            model_name='fm16',
            name='donation_type',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'Registered_organisation', b'Registered_organisation'), (b'Other_organisation', b'Other_organisation')]),
        ),
        migrations.AddField(
            model_name='fm16',
            name='f_bank',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fm16',
            name='f_dept',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fm16',
            name='f_designation',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fm16',
            name='f_id',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fm16',
            name='f_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fm16',
            name='f_pan',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fm16',
            name='medi_type',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'Normal', b'Normal'), (b'Parent_seniorctzn', b'Parent_seniorctzn'), (b'Parent_non_seniorctzn', b'Parent_non_seniorctzn')]),
        ),
        migrations.AlterField(
            model_name='fm16',
            name='assessment_year',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'Y2018_2019', b'Y2018_2019'), (b'Y2017_2018', b'Y2017_2018'), (b'Y2016_2017', b'Y2016_2017')]),
        ),
        migrations.AlterField(
            model_name='fm16',
            name='desig_employer',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fm16',
            name='edu_expense',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fm16',
            name='edu_loan',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fm16',
            name='us_10_14',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fm16',
            name='us_17_2',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
