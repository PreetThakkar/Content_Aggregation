from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import re

class Medium:
	feeds = {}

	def getFeeds(self):
		# Scraping Feed links
		response = requests.get("https://medium.com/topics")
		soup = BeautifulSoup(response.text, 'lxml')
		for element in soup.find_all('div', attrs = {"class": "streamItem streamItem--section js-streamItem"}):
			for i in element.find_all('a'):
				if i.string == None:
					# Was encountering Technology link twice. 
					# Once with None key. 
					# Once with proper 'Technology' as key
					continue
				self.feeds[i.string] = "https://medium.com/feed/" + i.get("href").split('.com/')[1]

	def getLinks(self, category = "Programming"):
		links = []
		if self.feeds == {} : response = requests.get("https://medium.com/feed/topic/programming")
		else : response = requests.get(self.feeds[category])
		xml = ET.fromstring(response.content)
		for item in xml.findall("./channel/item"):
			links.append( (item.find('title').text, item.find('link').text) )
		return {category: links}

	def getAll(self):
		self.getFeeds()
		for feed in self.feeds:
			yield {feed: self.getLinks(feed)[feed]}

# for cat in Medium().getAll():
# 	print(cat)