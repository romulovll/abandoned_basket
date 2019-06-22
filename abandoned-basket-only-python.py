#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime
import datetime
import json
import shutil

#Open JSON file
with open('input/page-views.json') as json_file:
    json_list = [json.loads(line) for line in json_file]

#Convert List in Dict
json_dict = { i : json_list[i] for i in range(0, len(json_list) ) }

for json_item in json_dict:
	if json_item +1 < len (json_dict):
	
		#Valida se o tempo de sessão de 10mim expirou
		if json_dict[json_item]['customer'] == json_dict[json_item +1]['customer']:
			diff_time = datetime.datetime.strptime(json_dict[json_item]['timestamp'], '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(json_dict[json_item +1]['timestamp'], '%Y-%m-%d %H:%M:%S')
			diff_time_minutes = diff_time.total_seconds() / 60 * -1
			
			if diff_time_minutes > float(10):
				print(json_dict[json_item]['customer'] +" "+ json_dict[json_item]['timestamp'] + " "+ json_dict[json_item]['page'])
				abandoned_cart = open('output/abandoned.json', 'a')
				abandoned_cart.write(str(json_dict[json_item])+'\n')
		
		#Verifica se o ultimo elemento no dict fez checkout
		else:
			if json_dict[json_item]['page'] !='checkout':
				abandoned_cart = open('output/abandoned.json', 'a')
				abandoned_cart.write(str(json_dict[json_item])+'\n')
				print(json_dict[json_item-1]['customer'] +" "+ json_dict[json_item-1]['timestamp'] + " "+ json_dict[json_item-1]['page'])
				print(json_dict[json_item]['customer'] +" "+ json_dict[json_item]['timestamp'] + " "+ json_dict[json_item]['page'])

