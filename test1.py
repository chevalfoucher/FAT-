# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 00:10:21 2015

@author: foucher
"""

import requests
api_key= "f2ef2c400800b31760e61f0485840562746676c9"
api_key_var = "?apiKey="
url_stations = "https://api.jcdecaux.com/vls/v1/stations"+api_key_var+api_key
url_contracts = "https://api.jcdecaux.com/vls/v1/contracts"+api_key_var+api_key
url_station1="https://api.jcdecaux.com/vls/v1/stations/1?contract=Rouen&apiKey="+api_key
headers = {'Accept': 'application/json'}
query_response_stations = requests.get(url_stations,headers=headers)
query_response_contracts = requests.get(url_contracts,headers=headers)
query_station1=requests.get(url_station1,headers=headers)
print query_response_stations
#print query_response_stations.text

#print query_response_contracts.text

print query_station1.text