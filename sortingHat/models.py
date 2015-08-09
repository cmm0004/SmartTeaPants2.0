from django.db import models
from sortingHat.helpers.modelToArray import ModelDataToArray

# Create your models here.
#most recent addition will be user.objects.first()
class User(models.Model):
	"""
	A User is a follower that has had their Data collected
	"""
	user_id = models.IntegerField(primary_key = True)
	screen_name = models.CharField(max_length = 50)
	contributors_enabled = models.BooleanField()
	hours_since_last_tweet = models.IntegerField(null=True)
	declared_blogger = models.BooleanField()
	declared_company = models.BooleanField()
	num_entities = models.IntegerField()
	tweets_favorited = models.IntegerField()
	num_followers = models.IntegerField()
	num_friends = models.IntegerField()
	geo_enabled = models.BooleanField()
	is_translator = models.BooleanField()
	listed_count = models.IntegerField()
	protected = models.BooleanField()
	num_tweets = models.IntegerField()
	has_profile_url = models.BooleanField()
	verified = models.BooleanField()

	def __str__(self):
		return self.screen_name

	def get_data(self, user_object):
		array_maker = ModelDataToArray()

		return array_maker.get_user_data(user_object)

	# def saveFromFollowers(self, TWEET_BOT, userid):
		
	# 	user_obj = TWEET_BOT.get_user(id=userid)
		
	# 	if user_obj.lang == 'en':
	# 		hourdelta = self._getHourDeltaRecentTweet(BOT=TWEET_BOT, userobject=user_obj)
			
	# 		row = User(contributors_enabled = not not user_obj.contributors_enabled, #contributers_enabled
	# 				hours_since_last_tweet = hourdelta, #hours_since_last_tweet
	# 				declared_blogger = self._parseDescriptionBlogger(userDescription=user_obj.description), #declared_blogger
	# 				declared_company = self._parseDescriptionCompany(userDescription=user_obj.description), #declared_company
	# 				num_entities = len(user_obj.entities), #num_entities
	# 				tweets_favorited = user_obj.favourites_count, #tweets_favorited
	# 				num_followers = user_obj.followers_count, #num_followers
	# 				num_friends = user_obj.friends_count, #num_friends
	# 				geo_enabled = not not user_obj.geo_enabled, #geo_enabled
	# 				is_translator = not not user_obj.is_translator, #is_translator
	# 				listed_count = user_obj.listed_count, #listed_count
	# 				protected = not not user_obj.protected, #protected
	# 				num_tweets = user_obj.statuses_count, #num_tweets
	# 				has_profile_url = not not user_obj.url, #has_profile_url
	# 				verified = not not user_obj.verified, #verified
	# 				screen_name = user_obj.screen_name, #screen_name, for my usage
	# 				user_id = user_obj.id) #id, for debugging
	# 		try:
	# 			print(row)
	# 			row.save()
	# 			return True
	# 		except IntegrityError as e:
	# 			print(e)
	# 			return False

class TrainingData(models.Model):
	"""
	TrainingData is a classified User
	0 - individual
	1 - business
	2 - blogger
	"""
	user = models.OneToOneField(User)
	classification = models.CharField(max_length=50)

	def __str__(self):
		return self.user.screen_name + " - " + self.classification

	
	def saveClassified(self, user, classification):
		row = TrainingData(
			user=user,
			classification=classification)

		row.save()

		return row


	def get_targets(self):
		td = self.objects.all()
		array_maker = ModelDataToArray(td)
		return array_maker.get_targets()
	##got the targets, next time get the data
	
	def get_data(self):
		td = self.objects.all()
		array_maker = ModelDataToArray(td)

		return array_maker.get_data()
