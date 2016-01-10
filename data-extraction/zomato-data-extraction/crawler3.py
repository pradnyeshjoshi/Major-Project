import urllib
import pycurl
import json

from pymongo import MongoClient

def getReviews(url):

    client = MongoClient()
    db = client.zomato
    collection = db.reviews

    pycurl_connect = pycurl.Curl()
    pycurl_connect.setopt(pycurl.URL, url)
    pycurl_connect.setopt(pycurl.HTTPHEADER, ['X-Zomato-API-Key: 7749b19667964b87a3efc739e254ada2'])

    with open('/Users/prady/Desktop/output.txt', 'w') as f:
        pycurl_connect.setopt(pycurl_connect.WRITEFUNCTION, f.write)
        pycurl_connect.perform()

    with open('/Users/prady/Desktop/output.txt') as data_file:    
        data = json.load(data_file)


    null=0

    review_entities = {}
    reviews = []
    list1 = []
    k=0
    num_records=0
    for keys in data:
        if keys == "userReviews":
            for result in data[keys]:
                for key1 in result:
                    #print (key1)
                    for vals in result[key1]:
                        ids = result[key1]
                        if vals == 'id':
                            #print (ids[vals])
                            list1.append({'id':ids[vals]})
                            num_records = num_records + 1
                        if vals == 'userName':
                            #print (ids[vals])
                            list1.append({'userName':ids[vals]})
                        if vals == 'rating_5':
                            #print (ids[vals])
                            list1.append({'rating_5':ids[vals]})
                        if vals == 'reviewText':
                            #print (ids[vals])
                            list1.append({'reviewText':ids[vals]})
                        if vals == 'reviewTime':
                            #print (ids[vals])
                            list1.append({'reviewTime':ids[vals]})
                    k=k+1
                    review_entities[str(k)]=list1
                    list1=[]


    #print (" ++hotel_entities++ ",review_entities)



    for item1 in review_entities:
    	items = {'ids':str(item1), 'userName':review_entities[item1][0]['userName'], 'rating_5':review_entities[item1][1]['rating_5'], 'reviewText':review_entities[item1][2]['reviewText'], 'reviewTime':review_entities[item1][3]['reviewTime'], 'id':review_entities[item1][4]['id']}
    	db.reviews.insert(items)
    '''	
    for num in range(1,num_records):
    	#print ("++ num ++ ",num)	
    	output = db.reviews.find_one({"ids":str(num)})
    	#print (output)
    	#print (output[output['ids']])
    	out2 = output[output['ids']]
    	#print (type(out2))
    	for hotel_id in out2:
    		for keys in hotel_id:
    			if keys == 'id':
    				#print (hotel_id[keys])
    				url =  url = "https://api.zomato.com/v1/reviews.json/"+str(hotel_id[keys])+"/user?count=5"
    				print(url)

    '''
