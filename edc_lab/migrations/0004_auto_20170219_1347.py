# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-19 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edc_lab', '0003_auto_20170219_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manifest',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edc_lab.Destination', verbose_name='Ship to'),
        ),
    ]
