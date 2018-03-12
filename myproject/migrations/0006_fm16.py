# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0005_auto_20170309_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fm16',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assessment_year', models.CharField(blank=True, max_length=200, null=True, choices=[(b'Y20182019', b'Y20182019'), (b'Y20172018', b'Y20172018'), (b'Y20162017', b'Y20162017')])),
                ('g_salary', models.CharField(max_length=200, null=True, blank=True)),
                ('p_tax', models.CharField(max_length=200, null=True, blank=True)),
                ('i_tax_paid', models.CharField(max_length=200, null=True, blank=True)),
                ('bank_interest', models.CharField(max_length=200, null=True, blank=True)),
                ('us_17_2', models.DateField(null=True, blank=True)),
                ('us_17_3', models.CharField(max_length=200, null=True, blank=True)),
                ('other_income', models.CharField(max_length=200, null=True, blank=True)),
                ('gpf', models.CharField(max_length=200, null=True, blank=True)),
                ('ppf', models.CharField(max_length=200, null=True, blank=True)),
                ('gis', models.CharField(max_length=200, null=True, blank=True)),
                ('lic', models.CharField(max_length=200, null=True, blank=True)),
                ('pli', models.CharField(max_length=200, null=True, blank=True)),
                ('edu_expense', models.DateField(null=True, blank=True)),
                ('hbl_principal', models.CharField(max_length=200, null=True, blank=True)),
                ('mf', models.CharField(max_length=200, null=True, blank=True)),
                ('nsc', models.CharField(max_length=200, null=True, blank=True)),
                ('sukanya', models.CharField(max_length=200, null=True, blank=True)),
                ('other_savings_name', models.CharField(max_length=200, null=True, blank=True)),
                ('other_savings', models.CharField(max_length=200, null=True, blank=True)),
                ('mediclaim', models.CharField(max_length=200, null=True, blank=True)),
                ('edu_loan', models.DateField(null=True, blank=True)),
                ('hbl_interest', models.CharField(max_length=200, null=True, blank=True)),
                ('donation', models.CharField(max_length=200, null=True, blank=True)),
                ('other_80_name_1', models.CharField(max_length=200, null=True, blank=True)),
                ('other_80_1', models.CharField(max_length=200, null=True, blank=True)),
                ('other_80_name_2', models.CharField(max_length=200, null=True, blank=True)),
                ('other_80_2', models.CharField(max_length=200, null=True, blank=True)),
                ('house_rent_exempt', models.CharField(max_length=200, null=True, blank=True)),
                ('us_10_14', models.DateField(null=True, blank=True)),
                ('tax_relief_89', models.CharField(max_length=200, null=True, blank=True)),
                ('relief_80ccc', models.CharField(max_length=200, null=True, blank=True)),
                ('relief_80ccd', models.CharField(max_length=200, null=True, blank=True)),
                ('name_employee', models.CharField(max_length=200, null=True, blank=True)),
                ('desig_employee', models.CharField(max_length=200, null=True, blank=True)),
                ('pan_employee', models.CharField(max_length=200, null=True, blank=True)),
                ('name_employer', models.CharField(max_length=200, null=True, blank=True)),
                ('desig_employer', models.DateField(null=True, blank=True)),
                ('tan_employer', models.CharField(max_length=200, null=True, blank=True)),
                ('pan_employer', models.CharField(max_length=200, null=True, blank=True)),
                ('date_employer_sign', models.CharField(max_length=200, null=True, blank=True)),
                ('place_employer_sign', models.CharField(max_length=200, null=True, blank=True)),
                ('name_employer_father', models.CharField(max_length=200, null=True, blank=True)),
                ('truck_image', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Load Details',
            },
        ),
    ]
