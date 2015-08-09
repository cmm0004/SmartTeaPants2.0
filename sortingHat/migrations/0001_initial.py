# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingData',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('classification', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('screen_name', models.CharField(max_length=50)),
                ('contributors_enabled', models.BooleanField()),
                ('hours_since_last_tweet', models.IntegerField(null=True)),
                ('declared_blogger', models.BooleanField()),
                ('declared_company', models.BooleanField()),
                ('num_entities', models.IntegerField()),
                ('tweets_favorited', models.IntegerField()),
                ('num_followers', models.IntegerField()),
                ('num_friends', models.IntegerField()),
                ('geo_enabled', models.BooleanField()),
                ('is_translator', models.BooleanField()),
                ('listed_count', models.IntegerField()),
                ('protected', models.BooleanField()),
                ('num_tweets', models.IntegerField()),
                ('has_profile_url', models.BooleanField()),
                ('verified', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='trainingdata',
            name='user',
            field=models.OneToOneField(to='sortingHat.User'),
        ),
    ]
