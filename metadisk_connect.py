#!/usr/bin/env python


import requests
import shutil
from PIL import Image   

class metadisk_connect:
	
	
	#~ metadisk_server = 'http://node1.metadisk.org/api/'
	#~ download_command = 'download/'

	def __init__(self):
	    self.metadisk_server = 'http://node1.metadisk.org/api/'
	    self.download_command = 'download/'
	    self.upload_command = 'upload'
	    
		
	def download_image(self,file_hash):
		download_url = self.metadisk_server +  self.download_command + file_hash
		print download_url
		response = requests.get(download_url, stream=True)
		with open('img.png', 'wb') as out_file:
		    shutil.copyfileobj(response.raw, out_file)
		del response
		img = Image.open("img.png")
		img.show() 
		
		
	def show_image(self,image_response):
		with open('img.png', 'wb') as out_file:
		    shutil.copyfileobj(image_response.raw, out_file)
		del image_response
		img = Image.open("img.png")
		img.show() 
		
	def download_file(self,file_hash):
		download_url = self.metadisk_server +  self.download_command + file_hash
		print "now downloading " + download_url
		response = requests.get(download_url, stream=True)
		return response
		
	def run_script(self,script_hash):
		print "running script"
		
	def upload_new_file(self):
		upload_url = self.metadisk_server +  self.upload_command 
		print upload_url
		files = {'file': open('site.wavesite', 'rb')}
		r = requests.post(upload_url, files=files)
		return r.text

		

