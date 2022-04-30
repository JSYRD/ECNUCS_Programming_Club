from encodings import utf_8
from ipaddress import ip_address
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

users = {'YRD':'password'}
guests = {'test':'test'}

@app.route('/api/login', methods = ["GET"])
def login():
    return_dict = {'code':'0', 'result':'true'}
    if(len(request.args)==0): 
        return_dict['result'] = 'false'
        return_dict['code'] = '404'
        return jsonify(return_dict)
    getData = request.args.to_dict()
    userName = getData.get('userName')
    userPassword = getData.get('userPassword')
    if(userName in users.keys() and (users[userName] == userPassword)):
        return jsonify(return_dict)
    else :
        return_dict['result'] = 'false'
        return_dict['code'] = '404'
        return jsonify(return_dict)

@app.route('/api/addGuest/',methods=['POST'])
def addGuest():
    return_dict = {'code':'0'}
    if(request.data):
        getData = json.loads(request.data.decode("utf-8"))
        guestName = getData.get('guestName')
        guestPassword = getData.get('guestPassword')
        guests[guestName] = guestPassword
        return jsonify(return_dict)
    return_dict['code'] = '404'
    return jsonify(return_dict)

@app.route('/api/getGuests', methods=['GET'])
def getGuests():
    return_dict = {'code':0, 'guests':guests}
    return jsonify(return_dict)

@app.route('/')
def index():
    return "Hello world!"


if(__name__ == '__main__'):
    app.run('localhost', debug=True)
