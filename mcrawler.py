import urllib, urllib2, HTMLParser
from bs4 import BeautifulSoup

class parseText(HTMLParser.HTMLParser):
	def handle_data(self, data):
		if data!= '\n':
			urlText.append(data)

class htmlCode(object):
	html = "h"
	hey = "this is a test string"
	def __init__(self, address):
		self.address = address
		self.address
		
	def visit_address(self):
		site_pointer = urllib.urlopen(self.address)
		self.html = site_pointer.read()
		self.html = self.clean_info(self.html)
	
	def clean_info(self, html):
		soup = BeautifulSoup(self.html)
		holder = soup.prettify().encode('utf-8')
		return holder
		
print "##########################"
print "# Africana Crawler 1.x.0 #"
print "##########################"
print ""
urlText=[]
lParser = parseText()
weblink = raw_input("Please enter the URL you wish to crawl: ")
print "Currently opening", weblink
code = htmlCode(weblink)
code.visit_address()
print "This is the code"
print code.html
#lParser.feed(code.html)
#lParser.close()
