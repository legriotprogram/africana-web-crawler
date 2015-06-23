import HTMLParser, urllib

urlText=[]

class parseText(HTMLParser.HTMLParser):
	def handle_data(self, data):
		if data!= '\n'
			urlText.append(data)
			
weblink = raw_input("Please enter the URL you wish to crawl:") # asks the user for a url 
print "Currently opening", weblink	# prints out the url entered -- for testing purposes (FTPs)
handle = urllib.urlopen(weblink)	# creates a variable handle which points to the url of interest
html_gunk = handle.read() 		# sets a string 'html_gunk' equal to the html content read from the page
