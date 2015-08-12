# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingTweet',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('polarity', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('user_id', models.IntegerField()),
                ('text', models.CharField(max_length=200)),
                ('parsed_text', models.CharField(max_length=200)),
                ('retweeted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='trainingtweet',
            name='tweet',
            field=models.OneToOneField(to='library.Tweet'),
        ),
    ]
