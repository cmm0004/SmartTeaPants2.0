import csv
from sortingHat.models import User, TrainingData

with open('sortingHat/TweetDataRedo.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		if row[3] == '?':
			row[3] = None
		new_user = User(
			screen_name = row[0], #screen_name
			user_id = row[1], #user_id
			contributors_enabled = row[2], #contributors_enabled
			hours_since_last_tweet = row[3], #hours_since_last_tweet
			declared_blogger = row[4], #declared_blogger
			declared_company = row[5], #declared_company
			num_entities = row[6], #num_profile_entities
			tweets_favorited  = row[7], #tweets_favorited
			num_followers = row[8], #num_followers
			num_friends = row[9], #num_friendships
			geo_enabled = row[10], #geo_enabled
			is_translator = row[11], #is_translator
			listed_count = row[12], #listed_count
			protected = row[13], #protected
			num_tweets = row[14], #num_tweets
			has_profile_url = row[15], #has_profile_url
			verified = row[16]) #verifed
		new_user.save()

		new_classified_user = TrainingData(
			user = new_user,
			classification = row[17])
		
		new_classified_user.save()

