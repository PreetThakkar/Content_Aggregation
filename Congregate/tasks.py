from celery import shared_task
from .feeds import * 
import csv
import shutil
import os

@shared_task
def storee(request):
	with open('temp.csv', 'w', encoding='utf-8', newline='') as f:
		writer = csv.writer(f)
		objects = [byteiota.Byteiota(), bbc.BBC(), engadget.Engadget(), medium.Medium()]
		data = []
		for object in objects:
			for result in object.getAll():
				data.append(result)
		writer.writerows(data)
	try:
		os.path.isfile('./data_new.csv')
		shutil.move('./data_new.csv', './data_old.csv')
	except Exception as e:
		pass
	shutil.move("./temp.csv", "./data_new.csv")
	return True