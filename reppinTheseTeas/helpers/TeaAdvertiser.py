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
		if self.today.day % 7 == 0:
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
		if self.today.day % 6 == 0:
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
