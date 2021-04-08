import xml.etree.ElementTree as ET
import requests

class BBC:
	feeds = {
		"Top" : "http://feeds.bbci.co.uk/news/rss.xml",
		"World" : "http://feeds.bbci.co.uk/news/world/rss.xml",
		"Business" : "http://feeds.bbci.co.uk/news/business/rss.xml",
		"Politics" : "http://feeds.bbci.co.uk/news/politics/rss.xml",
		"Health" : "http://feeds.bbci.co.uk/news/health/rss.xml",
		"Education Health" : "http://feeds.bbci.co.uk/news/education/rss.xml",
		"Science Environment" : "http://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
		"Technology" : "http://feeds.bbci.co.uk/news/technology/rss.xml",
		"Entertainment Arts" : "http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml"
	}		

	def getAll(self):
		for feed, rss in self.feeds.items():
			response = requests.get(rss)
			links = []
			# link structure
			# [ (feed, title, url) ]
			xml = ET.fromstring(response.content)
			for item in xml.findall("./channel/item"):
				yield ("BBC", feed, item.find('title').text, item.find('link').text)

# for cat in BBC().getAll():
# 	print(cat)