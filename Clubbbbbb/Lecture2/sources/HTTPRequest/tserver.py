from flask import Flask, request, jsonify
import json
app = Flask(__name__)

@app.route('/',methods = ["GET"])
def index():
    getData = request.args.to_dict()
    digit = int(getData.get('digit'))
    ret = str(digit**2)
    return ret

if(__name__ == '__main__'):
    app.run('localhost', debug=True)