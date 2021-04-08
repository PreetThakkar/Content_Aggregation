from feeds import *
import csv
import time
start_time = time.time()
objects = [bbc.BBC(), engadget.Engadget(), medium.Medium(), byteiota.Byteiota()]
f = open('data.csv', 'w', encoding='utf-8', newline='')
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