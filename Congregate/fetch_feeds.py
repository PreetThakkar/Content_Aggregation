from feeds import *
import time
start_time = time.time()
objects = [bbc.BBC(), engadget.Engadget(), medium.Medium(), byteiota.Byteiota()]
for object in objects:
	for result in object.getAll():
		pass
print("--- %s seconds ---" % (time.time() - start_time))
