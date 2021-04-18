from celery import shared_task
from .feeds import * 
import csv
import os

@shared_task
def storee(request):
	with open('temp.csv', 'w', encoding='utf-8', newline='') as f:
		writer = csv.writer(f)
		objects = [bbc.BBC(), engadget.Engadget(), medium.Medium(), byteiota.Byteiota()]
		data = []
		for object in objects:
			for result in object.getAll():
				data.append(result)
		writer.writerows(data)
	try:
		os.path.isfile('./data_new.csv')
		os.rename('./data_new.csv', './data_old.csv')
	except Exception as e:
		pass
	os.rename("./temp.csv", "./data_new.csv")
	return True