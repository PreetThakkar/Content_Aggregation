from bs4 import BeautifulSoup
import urllib.request as req
import requests

class Byteiota:

	feeds = {}

	def get_feeds(self):
		response = requests.get("https://byteiota.com/")
		soup = BeautifulSoup(response.content, "lxml")
		for a in soup.find('div', attrs = {'id': "categories-4"}).ul.find_all('a'):
			self.feeds[a.string] = a.get('href')

	def getAll(self):
		self.get_feeds()
		for feed, link in self.feeds.items():
			response = requests.get(link)
			soup = BeautifulSoup(response.content, "lxml")
			for h in soup.find_all('h3', attrs = {'class': 'post__title typescale-2'}):
				x = h.find('a')
				yield ("Byteiota", feed, x.string, x.get('href')) 
