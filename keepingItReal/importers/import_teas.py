import csv
from reppinTheseTeas.models import Tea

with open('reppinTheseTeas/helpers/Teas.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		new_tea = Tea(
			name = row[0], #name
			tea_type = row[1],
			month_available = row[2],
			steep_time = row[3],
			steep_temp = row[4])
			
		new_tea.save()