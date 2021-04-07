from feeds import *


if __name__ == '__main__':
	objects = [bbc.BBC(), byteiota.Byteiota(), engadget.Engadget(), medium.Medium()]
	for object in objects:
		print("\n\n")
		for result in object.getAll():
			for key, value in result.items():
				print("\n")
				print(object.__class__.__name__, key)
				print(*value, sep = "\n")

