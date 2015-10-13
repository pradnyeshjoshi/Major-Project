import urllib
import pycurl
import json

from pymongo import MongoClient

client = MongoClient()
db = client.zomato
collection = db.city


city_entities = {}
list1 = []
k=0

#url = "https://api.zomato.com/v1/reviews.json/1188/user?count=5"
url = "https://api.zomato.com/v1/cities.json"
#url = "https://api.zomato.com/v1/search.json?city_id=1"#&cuisine_id=55&category=2&start=1&count=10"

'''
pycurl_connect = pycurl.Curl()
pycurl_connect.setopt(pycurl.URL, url)
pycurl_connect.setopt(pycurl.HTTPHEADER, ['X-Zomato-API-Key: 7749b19667964b87a3efc739e254ada2'])

with open('/Users/prady/Desktop/output.txt', 'w') as f:
    pycurl_connect.setopt(pycurl_connect.WRITEFUNCTION, f.write)
    pycurl_connect.perform()
'''

with open('/Users/prady/Desktop/1.txt') as data_file:    
    data = json.load(data_file)
    #data = data_file.read()
#data=str(data)
#print(data)
#print(type(data))

#data = pycurl_connect.perform()

#print (data)
#print ("\nthe end\n")

null=0
num_records = 0

for keys in data:

    for value in data[keys]:

        for city in value:

            for vals in value[city]:
                
                ids = value[city]
                if vals == 'id':
                    #print ("id is ",ids[vals])
                    list1.append({'id':ids[vals]})
                    num_records = num_records + 1
                if vals == 'name':
                    #print ("name is",ids[vals])
                    list1.append({'name':ids[vals]})
            #list1.append(cities)
                #if 'data' in city_entities:
            k=k+1
            city_entities[str(k)]=list1
            list1=[]

#k=k+1
#city_entities[k]=list1            
#print (city_entities)
#print(num_records)

for item in city_entities:
	#print (item)
	items = {'ids':str(item),str(item):city_entities[item]}
	db.city.insert(items)
	#print("++ items ++ ",items)
for num in range(1,num_records):
	#print ("++ num ++ ",num)	
	output = db.city.find_one({"ids":str(num)})
	#print (output)
	#print (output[output['ids']])
	out2 = output[output['ids']]
	#print (type(out2))
	for city_id in out2:
		for keys in city_id:
			if keys == 'id':
				print (city_id[keys])
				url =  "https://api.zomato.com/v1/search.json?city_id="+str(city_id[keys])
				print(url)
