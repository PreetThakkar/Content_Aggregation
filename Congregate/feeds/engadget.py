import requests
import xml.etree.ElementTree as ET

class Engadget:
	'''
	This class is just one category. Gadgets.
	'''
	def getLinks(self):
		response = requests.get("https://www.engadget.com/rss.xml")
		links = []
		xml = ET.fromstring(response.content)
		for item in xml.findall("./channel/item"):
			links.append( (item.find('title').text, item.find('link').text) )
		return {"Engadget": links}

	def getAll(self):
		yield self.getLinks()

# for cat in Engadget().getAll():
# 	print(cat)