from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import re

class Medium:
	feeds = {}
	feeds = {
		"Art": "https://medium.com/feed/topic/art",
		"Books": "https://medium.com/feed/topic/books",
		"Gaming": "https://medium.com/feed/topic/gaming",
		"Podcasts": "https://medium.com/feed/topic/podcasts",
		"Fitness": "https://medium.com/feed/topic/fitness",
		"Health": "https://medium.com/feed/topic/health",
		"Business": "https://medium.com/feed/topic/business",
		"Design": "https://medium.com/feed/topic/design",
		"Freelancing": "https://medium.com/feed/topic/freelancing",
		"Product Management": "https://medium.com/feed/topic/product-management",
		"Remote Work": "https://medium.com/feed/topic/remote-work",
		"Startups": "https://medium.com/feed/topic/startups",
		"Creativity" :"https://medium.com/feed/topic/creativity",
		"Mindfulness": "https://medium.com/feed/topic/mindfulness",
		"Productivity": "https://medium.com/feed/topic/productivity",
		"Android Dev": "https://medium.com/feed/topic/android-development",
		"Data Science": "https://medium.com/feed/topic/data-science",
		"iOS Dev": "https://medium.com/feed/topic/ios-development",
		"Javascript": "https://medium.com/feed/topic/javascript",
		"Machine Learning": "https://medium.com/feed/topic/machine-learning",
		"Programming": "https://medium.com/feed/topic/programming",
		"Software Engineering": "https://medium.com/feed/topic/software-engineering",
		"Social Media": "https://medium.com/feed/topic/social-media",
		"World": "https://medium.com/feed/topic/world",
		"Artificial Intelligence": "https://medium.com/feed/topic/artificial-intelligence",
		"Blockchain": "https://medium.com/feed/topic/blockchain",
		"Cryptocurrency": "https://medium.com/feed/topic/cryptocurrency",
		"Cybersecurity": "https://medium.com/feed/topic/cybersecurity",
		"Digital Life": "https://medium.com/feed/topic/digital-life",
		"Gadgets": "https://medium.com/feed/topic/gadgets",
		"Privacy": "https://medium.com/feed/topic/privacy",
		"Self-Driving Cars": "https://medium.com/feed/topic/self-driving-cars",
		"Technology": "https://medium.com/feed/topic/technology",
	}

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
		# getFeeds will fetch all the feeds on Medium's website
		# self.getFeeds()
		for feed in self.feeds:
			yield {feed: self.getLinks(feed)[feed]}

Medium().getFeeds()