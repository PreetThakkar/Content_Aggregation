from bs4 import BeautifulSoup
import urllib.request as req
import requests

class Byteiota:

	feeds = {}

	def get_feeds(self):
		response = requests.get("https://byteiota.com/")
		soup = BeautifulSoup(response.content, "lxml")
		for x in soup.find('div', attrs = {'id': "categories-4"}).ul.find_all('li', recursive = False):
			self.feeds[x.a.string] = x.a.get('href')

	def getAll(self):
		self.get_feeds()
		for feed, link in self.feeds.items():
			response = requests.get(link)
			soup = BeautifulSoup(response.content, "lxml")
			for h in soup.find_all('h3'):
				if h.attrs['class'] == ['post__title', 'typescale-2'] or h.attrs['class'] == ['post__title', 'typescale-3']:
					x = h.find('a')	
					yield ("Byteiota", feed, x.string, x.get('href')) 

# if __name__ == '__main__':
# 	# byte = Byteiota()
# 	# byte.get_feeds()
# 	# print(*byte.feeds.items(), sep = '\n')
# 	for i in Byteiota().getAll():
# 		print(i)
