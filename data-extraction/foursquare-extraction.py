import json
import os
from pymongo import MongoClient

client = MongoClient()
db = client.foursquare
collection = db.user_tips

folder = os.path.join('/Users','prady','Desktop','major-project','DATA_FOURSQUARE','user','user-tips-cleaned')

files = os.listdir(folder)

review_id = None
review_text = ""
review_timestamp = None
location_id = None
location_name = ""

for user_file in files:
	path = '/Users/prady/Desktop/major-project/DATA_FOURSQUARE/user/user-tips-cleaned/' + user_file

	print("**************************************************************************************************************************")
	print(user_file)
	print("**************************************************************************************************************************")

	with open(path) as data_file:
		#print(path)
	    data = json.load(data_file)
	    user_tips_list=[]
	    for key_data in data:
			if key_data == 'response':
				for key_response in data.get(key_data):
					if key_response == 'tips':
						for key_tips in data.get(key_data).get(key_response):
							if key_tips == 'items':
								
								for counter in range(0,len(data.get(key_data).get(key_response).get(key_tips))):

									for key in data.get(key_data).get(key_response).get(key_tips)[counter]:

										if key == 'id':
											print('review id')
											print(data.get(key_data).get(key_response).get(key_tips)[counter].get(key))
											review_id = data.get(key_data).get(key_response).get(key_tips)[counter].get(key)

										if key == 'text':
											print('review text')
											print(data.get(key_data).get(key_response).get(key_tips)[counter].get(key))
											review_text = data.get(key_data).get(key_response).get(key_tips)[counter].get(key)

										if key == 'createdAt':
											print('review timestamp')
											print(data.get(key_data).get(key_response).get(key_tips)[counter].get(key))
											review_timestamp = data.get(key_data).get(key_response).get(key_tips)[counter].get(key)

										if key == 'venue':
											for key_venue in data.get(key_data).get(key_response).get(key_tips)[counter].get(key):
												if key_venue == 'id':
													print('location id')
													print(data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key_venue))
													location_id = data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key_venue)

												if key_venue == 'name':

													print('location name')
													print(data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key_venue))
													location_name = data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key_venue)

													user_tips_entry = {'review_id':str(review_id), 'location_id':str(location_id), 'review_text':review_text, 'review_timestamp':str(review_timestamp), 'location_name':location_name}
													user_tips_list.append(user_tips_entry)
	db_entry = {'user_id':str(user_file), 'user_tips_list':user_tips_list}
	db.user_tips.insert(db_entry)
'''

path = '/Users/prady/Desktop/major-project/DATA_FOURSQUARE/user/user-tips/132750'

with open(path) as data_file:
	data=json.load(data_file)

user_file=132750
print(user_file)
'''

