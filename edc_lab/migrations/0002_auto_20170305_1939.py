# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_lab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consignee',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='State or Province'),
        ),
        migrations.AddField(
            model_name='historicalconsignee',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='State or Province'),
        ),
        migrations.AddField(
            model_name='historicalshipper',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='State or Province'),
        ),
        migrations.AddField(
            model_name='shipper',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='State or Province'),
        ),
        migrations.AlterField(
            model_name='consignee',
            name='address',
            field=models.CharField(default='address', max_length=50, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consignee',
            name='city',
            field=models.CharField(default='city', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consignee',
            name='country',
            field=models.CharField(default='country', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consignee',
            name='postal_code',
            field=models.CharField(default='0000', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalconsignee',
            name='address',
            field=models.CharField(default='address', max_length=50, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalconsignee',
            name='city',
            field=models.CharField(default='city', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalconsignee',
            name='country',
            field=models.CharField(default='country', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalconsignee',
            name='postal_code',
            field=models.CharField(default='0000', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalshipper',
            name='address',
            field=models.CharField(default='address', max_length=50, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalshipper',
            name='city',
            field=models.CharField(default='city', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalshipper',
            name='country',
            field=models.CharField(default='country', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalshipper',
            name='postal_code',
            field=models.CharField(default='0000', max_length=50),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='address',
            field=models.CharField(default='address', max_length=50, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shipper',
            name='city',
            field=models.CharField(default='city', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shipper',
            name='country',
            field=models.CharField(default='country', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shipper',
            name='postal_code',
            field=models.CharField(default='0000', max_length=50),
        ),
    ]
