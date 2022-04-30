from flask import request
import requests
import json
# url='http://192.168.3.3:5000/api/addGuest/'
# data = {'guestName':'test0','guestPassword':'123'}
# print(json.dumps(data))
# res = requests.post(url=url, data = json.dumps(data))

url ='http://localhost:5000/api/login'
data = {'userName':'YRD','userPassword':'password'}
requests.get(url, json.dumps(data))