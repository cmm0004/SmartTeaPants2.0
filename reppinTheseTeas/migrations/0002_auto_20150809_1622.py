# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reppinTheseTeas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tea',
            name='tea_type',
            field=models.SmallIntegerField(),
        ),
    ]
