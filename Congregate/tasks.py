from celery import shared_task
from .feeds import * 
import csv
import shutil
import os

# @shared_task(name = 'fetch_news')
# def storee(request):
# 	with open('temp.csv', 'w', encoding='utf-8', newline='') as f:
# 		writer = csv.writer(f)
# 		objects = [byteiota.Byteiota(), bbc.BBC(), engadget.Engadget(), medium.Medium()]
# 		data = []
# 		for object in objects:
# 			for result in object.getAll():
# 				data.append(result)
# 		writer.writerows(data)
# 	try:
# 		os.path.isfile('./data_new.csv')
# 		shutil.move('./data_new.csv', './data_old.csv')
# 	except Exception as e:
# 		pass
# 	shutil.move("./temp.csv", "./data_new.csv")
# 	return True

@shared_task(name = 'test_celery')
def trial_test():
	print("Trial Test Executed.")

@shared_task(name = 'fetch_news')
def fetch_news():
	import csv
	import time
	start_time = time.time()
	objects = [bbc.BBC(), engadget.Engadget(), medium.Medium(), byteiota.Byteiota()]
	f = open('lol.csv', 'w', encoding='utf-8', newline='')
	writer = csv.writer(f)
	writer.writerow(["Source", "Feed / Category", "Title", "Url"])
	for object in objects:
		for result in object.getAll():
			try:
				writer.writerow(result)
			except UnicodeError as e:
				print(e)
				for i in result:
					print(type(i), i)
	print("--- %s seconds ---" % (time.time() - start_time))
	f.close()