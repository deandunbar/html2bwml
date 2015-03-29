#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

new = 1 # open in a new tab, if possible

class rewrite:
	default_url = "http://localhost:8080"
	get_url = "http://islandshare.rocks/"
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	
	
	#~ response = requests.get(url, headers=headers)
	
	#~ new = 2 # open in a new tab, if possible
	
		
		
	#~ def get_website(self):
		#~ soup = BeautifulSoup('<p>Blah blah blah <a href="http://google.com">Google</a></p>')
		#~ for a in soup.findAll('a'):
		    #~ a['href'] = a['href'].replace("google", "mysite")
		#~ print str(soup)
	
		
	def get_website(self,url):
		#~ print "now downloading " + url
		response = requests.get(url, headers = self.headers, stream=True)		
		soup = BeautifulSoup(response.text)
		#~ print str(response.text)
		return soup
		
		
	def rewrite_links(self, soup):
		#~ print "rewriting the html"
		for a in soup.findAll('a'):
			a['href'] = a['href'].replace("google", "mysite")
		#~ print str(soup)
		print soup


website_rewriter = rewrite()
soup = website_rewriter.get_website("http://www.useragentstring.com/")
print soup
#~ soup = website_rewriter.get_website("https://www.google.com/#q=food")
converted_file = website_rewriter.rewrite_links(soup)


