# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webdb', '0007_auto_20161118_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webdb.University'),
        ),
    ]
