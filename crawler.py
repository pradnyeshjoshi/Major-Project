#using zomato api's

import urllib
import pycurl


url = "https://api.zomato.com/v1/reviews.json/1188/user?count=100"

pycurl_connect = pycurl.Curl()
pycurl_connect.setopt(pycurl.URL, url)
pycurl_connect.setopt(pycurl.HTTPHEADER, ['X-Zomato-API-Key: 7749b19667964b87a3efc739e254ada2'])
pycurl_connect.perform()


#htmlfile = urllib.urlopen(url)
#htmltext = htmlfile.read()
#print (htmltext)
