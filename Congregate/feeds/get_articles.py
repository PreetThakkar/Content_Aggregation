import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import requests


class Scrapp:

    @staticmethod
    def getSoup(url: str) -> BeautifulSoup:
        response = requests.get(url, allow_redirects=True)
        return BeautifulSoup(response.text, 'lxml')

    @staticmethod
    def getXmlTree(rss: str) -> ET.Element:
        response = requests.get(rss)
        print(response.status_code)
        return ET.fromstring(response.text)


class BBC:
    feeds = {}

    def get_all_rss(self):
        soup = Scrapp.getSoup('https://www.bbc.co.uk/news/10628494#userss')
        links_list = soup.select_one('div.story-feature.wide ul')
        for link in links_list.select('a'):
            self.feeds[link.get_text()] = link.attrs['href']

    def getAll(self):
        self.get_all_rss()
        # link structure [ (BBC, feed, title, url) ]
        for feed, rss in self.feeds.items():
            xml = Scrapp.getXmlTree(rss)
            for item in xml.findall("./channel/item"):
                yield ("BBC", feed, item.find('title').text, item.find('link').text)


class Byteiota:

    feeds = {}

    def get_feeds(self):
        soup = Scrapp.getSoup("https://byteiota.com/")
        for x in soup.find('div', attrs={'id': "categories-4"}).ul.find_all('li', recursive=False):
            self.feeds[x.a.string] = x.a.get('href')

    def getAll(self):
        self.get_feeds()
        for feed, link in self.feeds.items():
            soup = Scrapp.getSoup(link)
            for h in soup.find_all('h3', {'class': ['post__title typescale-2', 'post__title typescale-3']}):
                x = h.find('a')
                yield ("Byteiota", feed, x.string, x.get('href'))


class Engadget:
    feeds = {"Engadget": "https://www.engadget.com/rss.xml"}

    def getAll(self):
        for _, rss in self.feeds.items():
            xml = Scrapp.getXmlTree(rss)
            for item in xml.findall("./channel/item"):
                yield ("Engadget", "Engadget", item.find('title').text, item.find('link').text)


class Medium:
    # feeds = {}
    feeds = {}

    def get_all_rss(self):
        # Scraping Feed links
        soup = Scrapp.getSoup("https://medium.com/topics")
        for element in soup.find_all('div', attrs={"class": "streamItem streamItem--section js-streamItem"}):
            for i in element.find_all('a'):
                if i.string == None:
                    # Was encountering Technology link twice. Once with None key. Once with proper 'Technology' as key
                    continue
                self.feeds[i.string] = "https://medium.com/feed/" + \
                    i.get("href").split('.com/')[1]

    def getAll(self):
        # getFeeds will fetch all the feeds on Medium's website
        self.get_all_rss()
        for feed, rss in self.feeds.items():
            xml = Scrapp.getXmlTree(rss)
            for item in xml.findall("./channel/item"):
                yield ("Medium", feed, item.find('title').text, item.find('link').text)

if __name__ == '__main__':
    for item in BBC().getAll():
        print(item)