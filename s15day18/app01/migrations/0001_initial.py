# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-06 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=32)),
                ('ip', models.CharField(max_length=32)),
                ('port', models.IntegerField(max_length=6)),
            ],
        ),
    ]
