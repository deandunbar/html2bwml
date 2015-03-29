#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import base64
import shutil
from PIL import Image   
import metadisk_connect
import json
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
		
	def get_image(self,url):
		response = requests.get(url, headers = self.headers, stream=True)
		with open('img.tmp', 'wb') as out_file:
		    shutil.copyfileobj(response.raw, out_file)
		del response
		img = Image.open("img.png")
		img.save("img.tmp", 'JPEG', quality=50)
		with open("img.tmp", "rb") as image_file:
		    encoded_string = base64.b64encode(image_file.read())
		#~ img = Image.open("img.tmp")
		#~ img.show()
		return encoded_string
		
	def rewrite_links(self, soup):
		#~ print "rewriting the html"
		for a in soup.findAll('a'):
			a['href'] = a['href'].replace("google", "mysite")
		#~ print str(soup)
		print soup
		
	def save_to_metadisk(self):
		
		mdc = metadisk_connect.metadisk_connect()
		uploaded_hash = mdc.upload_new_file()
		
		return uploaded_hash
		



	def textify_img(self,image_url):
		with open("yourfile.ext", "rb") as image_file:
		    encoded_string = base64.b64encode(image_file.read())
		
	def rewrite_to_bwml(self, url):
		soup = self.get_website(url)
		souper = soup.select("#bw_content")
		soup = souper[0]
		
		#~ print "rewriting the html"
		for a in soup.findAll('a'):
			a['href'] = a['href'].replace("google", "mysite")
		for tag in soup.findAll('img'):
			img_url = tag["src"]			
			base64_string = self.get_image(img_url)
			tag['src'] = str("data:image/png;base64," + base64_string)
		with open('site.wavesite', 'wb') as out_file:
		    out_file.write(str(soup))
		return soup
		
		



website_rewriter = rewrite()
#~ img_text = website_rewriter.get_image("http://i.imgur.com/tAHVmXi.jpg")
#~ print soup
bwml = website_rewriter.rewrite_to_bwml("http://islandshare.rocks")
new_file_info = website_rewriter.save_to_metadisk()
new_file_info = json.loads(new_file_info)
print new_file_info


