from celery import shared_task
from .feeds import * 
import csv

@shared_task
def storee(request):
	with open('data1.csv', 'w', encoding='utf-8', newline='') as f:
		writer = csv.writer(f)
		objects = [bbc.BBC(), engadget.Engadget(), medium.Medium(), byteiota.Byteiota()]
		data = []
		for object in objects:
			for result in object.getAll():
				data.append(result)
		writer.writerows(data)
	return True