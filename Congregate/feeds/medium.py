from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import re

class Medium:
	# feeds = {}
	feeds = {
		"Android Dev": "https://medium.com/feed/topic/android-development",
		"Data Science": "https://medium.com/feed/topic/data-science",
		"iOS Dev": "https://medium.com/feed/topic/ios-development",
		"Javascript": "https://medium.com/feed/topic/javascript",
		"Machine Learning": "https://medium.com/feed/topic/machine-learning",
		"Programming": "https://medium.com/feed/topic/programming",
		"Software Engineering": "https://medium.com/feed/topic/software-engineering",
		"Artificial Intelligence": "https://medium.com/feed/topic/artificial-intelligence",
		"Cybersecurity": "https://medium.com/feed/topic/cybersecurity",
		"Technology": "https://medium.com/feed/topic/technology",
	}

	def get_all_rss(self):
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


	def getAll(self):
		# getFeeds will fetch all the feeds on Medium's website
		# self.get_all_rss()
		for feed, rss in self.feeds.items():
			response = requests.get(rss)
			xml = ET.fromstring(response.content)
			for item in xml.findall("./channel/item"):
				yield ("Medium", feed, item.find('title').text, item.find('link').text)


# Medium().getFeeds()
# for results in Medium().getAll():
# 	for key, value in results.items():
# 		for i in value:
# 			print(i[0])
