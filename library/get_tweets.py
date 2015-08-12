import re
import tweepy
import time
import csv
from sortingHat.helpers.auth import API
from datetime import datetime
from sortingHat.helpers.search import Search


class TweetGrabber(object):

	api = API()
	BOT = api.authenticate()
	searcher = Search(BOT)


	statuses = searcher.get_statuses(query="#tea", count=20)
	for status in statuses:
		print(str(status.text) + "," + str(status.id) + "," + str(status.user.id))
			
	