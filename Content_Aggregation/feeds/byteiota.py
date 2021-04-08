from bs4 import BeautifulSoup
import urllib.request as req
import requests

class Byteiota:

	def getLinks(self):
		'''
		{
			"category_1" : [ ("title_1", "link_1"), ... ], 
			"category_2" : [ ("title_1", "link_1"), ... ], 
			...
		}
		'''
		response = requests.get("https://byteiota.com/")
		soup = BeautifulSoup(response.content, "lxml")
		categories = {}
		for a in soup.find('div', attrs = {'id': "categories-4"}).ul.find_all('a'):
			sub_response = requests.get(a.get('href'))
			sub_soup = BeautifulSoup(sub_response.content, "lxml")
			temp = []
			for h in sub_soup.find_all('h3', attrs = {'class': 'post__title typescale-2'}):
				x = h.find('a')
				temp.append((x.string, x.get('href')))
			if temp == []: categories[a.string] = [(a.string, a.get('href'))]
			else: categories[a.string] = temp
		return categories

	def getAll(self):
		yield self.getLinks()

# for cat in Byteiota().getAll():
# 	print(cat)