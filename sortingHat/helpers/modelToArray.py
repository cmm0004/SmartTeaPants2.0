import numpy as np

class ModelDataToArray(object):
	#array
	def __init__(self, model_data_query_set=[]):
		self.model_data = model_data_query_set

	def get_user_data(self, user_object):
		row = []
		data = [
			user_object.contributors_enabled,
			self._none_to_0(user_object.hours_since_last_tweet),
			user_object.declared_blogger,
			user_object.declared_company,
			user_object.num_entities,
			user_object.tweets_favorited,
			user_object.num_followers,
			user_object.num_friends,
			user_object.geo_enabled,
			user_object.is_translator,
			user_object.listed_count,
			user_object.protected,
			user_object.num_tweets,
			user_object.has_profile_url,
			user_object.verified]
		row.append(data)

		return np.array(row, dtype='int')

	def get_data(self):
		rows = []
		for model in self.model_data:
			data = [
			model.user.contributors_enabled,
			self._none_to_0(model.user.hours_since_last_tweet),
			model.user.declared_blogger,
			model.user.declared_company,
			model.user.num_entities,
			model.user.tweets_favorited,
			model.user.num_followers,
			model.user.num_friends,
			model.user.geo_enabled,
			model.user.is_translator,
			model.user.listed_count,
			model.user.protected,
			model.user.num_tweets,
			model.user.has_profile_url,
			model.user.verified
			]
			
			
			rows.append(data)

		return np.array(rows, dtype='int')

	def _none_to_0(self, data_point):
		if data_point == None:
			data_point = '0'
		return data_point

	def get_targets(self):
		targets = []
		for model in self.model_data:
			targets.append(model.classification)

		return np.array(targets)
