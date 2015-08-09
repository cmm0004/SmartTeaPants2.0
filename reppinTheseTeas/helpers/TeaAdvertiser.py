import datetime, tweepy
from reppinTheseTeas.models import Tea

class TeaAdvertiser(object):

	def __init__(self, BOT):
		self.BOT = BOT
		self.today = datetime.datetime.today()
		self.teas_out_now = Tea.objects.filter(month_available=self.today.month)
		
		last_month = self.today.month - 1
		self.teas_individual_available = Tea.objects.filter(month_available=last_month)

	def advertise_this_months(self):
	
		#this is the string, plus removing the apostrophes because the strings come back from the db in single quotes
		status = '{0}s #teas are {1} #{2}tea and {3} #{4}tea, read more here: www.teasontheloose.com/blog'.format(
			self.today.strftime('%B'),
			self.teas_out_now[0].name,
			self.teas_out_now[0].get_tea_type_name(),
			self.teas_out_now[1].name,
			self.teas_out_now[1].get_tea_type_name()).replace("'", "")
		
		try:
			self.BOT.update_status(status=status)
			print("Advertised tea")
			print(status)
		except tweepy.TweepError as e:
			print(e)
			print(status)

	def advertise_last_months(self):
		status = 'Cant get enough? Our {0} #{1}tea and {2} #{3}tea are now available to purchase individually!'.format(
			self.teas_individual_available[0].name,
			self.teas_individual_available[0].get_tea_type_name(),
			self.teas_individual_available[1].name,
			self.teas_individual_available[1].get_tea_type_name()).replace("'", "")
	
		try:
			self.BOT.update_status(status=status)
			print("Advertised individual tea")
			print(status)
		except tweepy.TweepError as e:
			print(e)
			print(status)

		try:
			self.BOT.update_status(status="Buy #teas from our last shipment individually here: www.teasontheloose.com/buy-individual")
			print("Advertised individual tea followup")
			print("Buy #teas from our last shipment individually here: www.teasontheloose.com/buy-individual")
		except tweepy.TweepError as e:
			print(e)
			print("Buy #teas from our last shipment individually here: www.teasontheloose.com/buy-individual")


#class WeekDayAware(object):

# 	def __init__(self):
# 		self.weekdays = ['monday', 'tuesday', 'wednesday',
# 		 'thursday', 'friday', 'saturday', 'sunday']
# 		self.today = datetime.datetime.today()
# 		self.today_int = self.today.weekday()
# 		self.today_str = self.weekdays[self.today_int]
# 		self.month_int = self.today.month

# 	def ff_get_status(self):
# 		users = User.objects.filter(classification='individual')
# 		if len(users) > 0:
# 			screennames = []
# 			for user in users:
# 				screennames.append('@' + user.screen_name)
			
# 			ff_status = "Happy #FF "
# 			while len(ff_status) < 140:
# 				if len(screennames) > 0:
# 					ff_status += screennames.pop()
# 					ff_status += " "
# 					continue
# 				break
# 			print('status for ff: ' + ff_status)
# 			return ff_status
# 		return False

# 	def buy_individual_status(self):
# 		if (self.today_int % 3) == 0:
# 			status = "#teasontheloose Just want one? Get a previous months' tea while supplies last here: www.teasontheloose.com/buy-individual.html"
			
# 			#you saved month index 0-11, datetime gives 1-12
			
# 			#queryObject
# 			teas = Tea.get_teas_available(Tea, (self.month_int - 2))
# 			if len(teas) == 2:
# 				status_followup = "www.teasontheloose.com/buy-individual.html This month's individual #teas are {} and {}".format(teas[0].name, teas[1].name)
# 				return status, status_followup
# 			print('put more teas in the database!')
# 		print('not the right day for individual sales tweets')
# 		return False, False