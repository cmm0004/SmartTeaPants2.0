import csv
from sortingHat.models import User, TrainingData
from django.db import IntegrityError


def import_from_csv(pathtofile):
	with open(pathtofile) as file:
		reader = csv.reader(file)
		for row in reader:
			new_classified_user = TrainingData(
				user = _get_user_object(row[1]),
				classification = row[2])
			try:
				new_classified_user.save()
			except IntegrityError as e:
				print(e)
				continue

def _get_user_object(screen_name):
	qs = User.objects.filter(screen_name=screen_name)
	if len(qs) > 0:
		return qs[0]