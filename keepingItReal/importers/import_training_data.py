import csv
from sortingHat.models import User, TrainingData
from django.db import IntegrityError


def import_from_csv(pathtofile):
	with open(pathtofile) as file:
		reader = csv.reader(file)
		for row in reader:
			td, created = TrainingData.objects.get_or_create(id=row[0])
			if not created:
				td.classification = row[2]
				try:
					td.save()
				except IntegrityError as e:
					print(e)
					continue
		