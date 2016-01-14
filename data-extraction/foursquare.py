import json
import os
from pymongo import MongoClient
#import time

client = MongoClient()
db = client.fs
#collection = db.tips

folder = os.path.join('/Users','prady','Desktop','major-project','DATA_FOURSQUARE','user','user-tips-cleaned')

files = os.listdir(folder)

review_id = None
review_text = ""
review_timestamp = None
location_id = None
location_name = ""
first_name = ""
last_name = ""

for user_file in files:

	col = user_file

	path = '/Users/prady/Desktop/major-project/DATA_FOURSQUARE/user/user-tips-cleaned/' + user_file

	#print("**************************************************************************************************************************")
	#print(user_file)
	#print("**************************************************************************************************************************")

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

										'''if key == 'photos':

											for key1 in data.get(key_data).get(key_response).get(key_tips)[counter].get(key):
												if key1 == 'groups':
													for counter2 in range(0,len(data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key1))):
														for key2 in data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key1)[counter2]:
															if key2 == 'items':
																for counter3 in range(0,len(data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key1)[counter2].get(key2))):
																	for key3 in data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key1)[counter2].get(key2)[counter3]:
																		if key3 == 'user':
																			for key4 in data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key1)[counter2].get(key2)[counter3].get(key3):
																				if key4 == 'firstName':
																					first_name = data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key1)[counter2].get(key2)[counter3].get(key3).get(key4)
																				if key4 == 'lastName':
																					last_name = data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key1)[counter2].get(key2)[counter3].get(key3).get(key4)'''


										if key == 'id':
											#print('review id')
											#print(data.get(key_data).get(key_response).get(key_tips)[counter].get(key))
											review_id = data.get(key_data).get(key_response).get(key_tips)[counter].get(key)

										if key == 'text':
											#print('review text')
											#print(data.get(key_data).get(key_response).get(key_tips)[counter].get(key))
											review_text = data.get(key_data).get(key_response).get(key_tips)[counter].get(key)

										if key == 'createdAt':
											#print('review timestamp')
											#print(data.get(key_data).get(key_response).get(key_tips)[counter].get(key))
											review_timestamp = data.get(key_data).get(key_response).get(key_tips)[counter].get(key)

										if key == 'venue':
											for key_venue in data.get(key_data).get(key_response).get(key_tips)[counter].get(key):
												if key_venue == 'id':
													#print('location id')
													#print(data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key_venue))
													location_id = data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key_venue)

												if key_venue == 'name':

													#print('location name')
													#print(data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key_venue))
													location_name = data.get(key_data).get(key_response).get(key_tips)[counter].get(key).get(key_venue)

													user_tips_entry = {'review_id':str(review_id), 'location_id':str(location_id), 'review_text':review_text, 'review_timestamp':str(review_timestamp), 'location_name':location_name}
													db[col].insert(user_tips_entry)
													#user_tips_list.append(user_tips_entry)
	#db_entry = {'user_id':str(user_file), 'user_tips_list':user_tips_list}
	#db.user_tips.insert(db_entry)
'''

path = '/Users/prady/Desktop/major-project/DATA_FOURSQUARE/user/user-tips/132750'

with open(path) as data_file:
	data=json.load(data_file)

user_file=132750
print(user_file)
'''

