# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0003_enrollment'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='cbook',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='vehicle_type',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'Canter Jumbo', b'Canter Jumbo'), (b'Canters 7.5MT/ 6 Wheel', b'Canters 7.5MT/ 6 Wheel'), (b'Containers Truck', b'Containers Truck'), (b'Low Bed Trailer', b'Low Bed Trailer'), (b'Mulit Axle Trailer', b'Mulit Axle Trailer')]),
        ),
    ]
