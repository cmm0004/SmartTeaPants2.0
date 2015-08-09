from django.db import models

# Create your models here.
class Tea(models.Model):
	"""
	A Tea is the info for a tea
	tea_type = 
	0 = white
	1 = green
	2 = oolong
	3 = black
	4 = dark
	5 = herbal
	"""
	name = models.CharField(max_length = 50)
	tea_type = models.SmallIntegerField()
	month_available = models.SmallIntegerField()
	steep_time = models.SmallIntegerField()
	steep_temp = models.SmallIntegerField()

	def __str__(self):
		return self.name

	def get_tea_type_name(self):
		if self.tea_type == 0:
			return 'white'
		elif self.tea_type == 1:
			return 'green'
		elif self.tea_type == 2:
			return 'oolong'
		elif self.tea_type == 3:
			return 'black'
		elif self.tea_type == 4:
			return 'dark'
		elif self.tea_type == 5:
			return 'herbal'
		else:
			return




