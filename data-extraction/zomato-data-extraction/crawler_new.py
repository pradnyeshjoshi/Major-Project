import urllib
import pycurl
import json
from pymongo import MongoClient
import crawler2
from crawler2 import *

client = MongoClient()
db = client.zomato
collection = db.city


city_entities = {}
list1 = []
k=0

url = "https://api.zomato.com/v1/cities.json"

pycurl_connect = pycurl.Curl()
pycurl_connect.setopt(pycurl.URL, url)
pycurl_connect.setopt(pycurl.HTTPHEADER, ['X-Zomato-API-Key: 7749b19667964b87a3efc739e254ada2'])

with open('/Users/prady/Desktop/output.txt', 'w') as f:
    pycurl_connect.setopt(pycurl_connect.WRITEFUNCTION, f.write)
    pycurl_connect.perform()

with open('/Users/prady/Desktop/output.txt') as data_file:    
    data = json.load(data_file)

null=0
num_records = 0

for keys in data:

    for value in data[keys]:

        for city in value:

            for vals in value[city]:
                
                ids = value[city]
                if vals == 'id':
                    list1.append({'id':ids[vals]})
                    num_records = num_records + 1
                if vals == 'name':
                    list1.append({'name':ids[vals]})
            k=k+1
            city_entities[str(k)]=list1
            list1=[]

for item in city_entities:
	items = {'ids':str(item),"id":city_entities[item][0]['id'], "name":city_entities[item][1]['name']}
	db.city.insert(items)
    
for num in range(1,num_records):
    output = db.city.find_one({"ids":str(num)})
    url =  "https://api.zomato.com/v1/search.json?city_id="+str(output['id'])
    getHotels(url)
