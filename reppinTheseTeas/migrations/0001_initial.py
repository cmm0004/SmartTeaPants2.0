# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('tea_type', models.CharField(max_length=50)),
                ('month_available', models.SmallIntegerField()),
                ('steep_time', models.SmallIntegerField()),
                ('steep_temp', models.SmallIntegerField()),
            ],
        ),
    ]
