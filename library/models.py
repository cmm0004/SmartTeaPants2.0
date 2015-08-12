from django.db import models
from sortingHat.models import User

# Create your models here.

class Tweet(models.Model):
	user_id = models.IntegerField()
	#status.user.id
	text = models.CharField(max_length=200)
	#status.text
	#parse_text is without hashtags or urls
	parsed_text = models.CharField(max_length=200)
	retweeted = models.BooleanField(default=False)

class TrainingTweet(models.Model):
	tweet = models.OneToOneField(Tweet)
	#0 is neg, 1 is pos
	polarity = models.SmallIntegerField()


