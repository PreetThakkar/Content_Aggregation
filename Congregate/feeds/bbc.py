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
		for feed in self.feeds:
			yield self.getLinks(feed)

	def getLinks(self, category = "Technology"):
		response = requests.get(self.feeds[category])
		links = []
		xml = ET.fromstring(response.content)
		for item in xml.findall("./channel/item"):
			links.append( (item.find('title').text, item.find('link').text) )
		return {category: links}

# for cat in BBC().getAll():
# 	print(cat)