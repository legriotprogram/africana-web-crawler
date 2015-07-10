import urllib, urllib.request, sys
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from re import sub

class parseText(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.data = ''
		self.counter = ""

	def handle_starttag(self, tag, attrs):
		if((tag == 'head' or tag == 'title' or tag == 'ol' or tag == 'dl' or tag == 'li' or tag == 'ul' or tag[0] == 'h') and tag != 'html'):
			self.counter = tag
			self.data += "<%s" %(tag,)
			if(attrs):
				self.data += " "+" ".join('%s="%s"' %(k,v) for k, v in attrs)
			self.data += ">"
			urlText.append(self.data)
		self.data = ''
	def handle_data(self,data):
		self.data +=data
		self.data = self.data.replace('\\n',"\n")
		self.data = self.data.rstrip('\n')
		self.data = sub("(\s)",'',self.data)
		
		if(self.data != '\n' and self.data != ''): 
			if(len(urlText) != 0):
				self.data = urlText.pop() +""+self.data+""
			urlText.append(self.data)
		self.data = ''

	def handle_endtag(self,tag):
		if((tag == 'head' or tag == 'title' or tag == 'ol' or tag == 'dl' or tag == 'li' or tag == 'ul' or tag[0] == 'h')and tag != 'html'):
			if(len(urlText) != 0 and self.counter == tag):
				self.data += urlText.pop()
			self.data += "</%s>" % (tag,)
			urlText.append(self.data)
		self.data = ''


class htmlCode(object):
	html = "h"
	hey = "this is a test string"
	def __init__(self, address):
		self.address = address
		self.address
		
	def visit_address(self):
		site_pointer = urllib.request.urlopen(self.address)
		self.html = site_pointer.read()
		self.html = self.clean_info(self.html)
	
	def clean_info(self, html):
		soup = BeautifulSoup(self.html, "html.parser")
		[s.extract() for s in soup.findAll('script')] #removes javascript
		[s.extract() for s in soup.findAll('style')] #removes javascript
		holder = soup.prettify().encode('utf-8')
		holder = str(holder)#decodes bytes to string
		return holder

		
print ("##########################")
print ("# Africana Crawler 1.x.0 #")
print ("##########################")
print ("")
urlText=[]

lParser = parseText()
weblink = input("Please enter the URL you wish to crawl: ") #raw_input
print ("Currently opening", weblink)
code = htmlCode(weblink)
code.visit_address()
#print ("This is the code")


lParser.feed(code.html)
lParser.close()
print("Parsed html")

for item in urlText:
	print (item)

