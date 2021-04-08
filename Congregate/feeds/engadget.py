import requests
import xml.etree.ElementTree as ET

class Engadget:
	'''
	This class is just one category. Gadgets.
	'''	
	feeds = {"Engadget" : "https://www.engadget.com/rss.xml"}

	def getAll(self):
		for feed, rss in self.feeds.items():
			response = requests.get(rss)
			links = []
			xml = ET.fromstring(response.content)
			for item in xml.findall("./channel/item"):
				links.append( ("Engadget", "Engadget", item.find('title').text, item.find('link').text) )
			yield links