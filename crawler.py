import HTMLParser, urllib

urlText=[]		# the collection of all the text from a given page

class parseText(HTMLParser.HTMLParser): # a class that extends the python HTMLParser
	def handle_data(self, data):		# this parser excludes empty line breaks
		if data != '\n':
			urlText.append(data)

lParser = parseText()	# initializes a text parser
weblink = raw_input("Please enter the URL you wish to crawl:") # asks the user for a url 
print "Currently opening", weblink	# prints out the url entered -- for testing purposes (FTPs)
site_pointer = urllib.urlopen(weblink) # creates a variable 'site_pointer' which points to the url of interest
raw_html = site_pointer.read() 		# sets a string 'raw_html' equal to the html content read from the page
lParser.feed(raw_html)				#feeds the raw html to our special html parser
lParser.close()			# closes the text parser
for item in urlText:	# prints out all the text read from the given page -- FTPs
	print item
