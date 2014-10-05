'''
@AUTHOR: Iris Yuan
A lazy solution to wanting Colbert tickets. 
If tickets are available, a window will pop up. 
Otherwise, check again in a minute. 
'''

from bs4 import BeautifulSoup
import urllib2
import webbrowser
import time

site = 'http://impresario.comedycentral.com/show/5b2eb3b0eb99f143'
available = False

def getHeaderMessage(url):

	# iframe div in http://thecolbertreport.cc.com/tickets stores ticket magic
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	body = BeautifulSoup(response.read())

	# if tickets aren't available, headerMessage says "We're sorry..." 
	return body.find("p", attrs = {"class" : "headerMessage"})

# if Colbert doesn't apologize, we can assume there are free tickets!

while (not available):
	if getHeaderMessage(site) == 'None':
		webbrowser.open_new('http://thecolbertreport.cc.com/tickets')
		available = True
	else:
		# Check again in a minute
		time.sleep(60)
