import urllib
import pycurl
import json
from pymongo import MongoClient
import crawler2
from crawler2 import *

url = "https://api.zomato.com/reviews?res_id=5800519"

pycurl_connect = pycurl.Curl()
pycurl_connect.setopt(pycurl.URL, url)
pycurl_connect.setopt(pycurl.HTTPHEADER, ['user_key: 7749b19667964b87a3efc739e254ada2'])

pycurl_connect.perform()


