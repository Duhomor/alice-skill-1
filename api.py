from __future__ import unicode_literals
import json
import logging
from flask import Flask, request
import csv

with open('ief.csv', newline='') as File:  
    reader = csv.reader(File)

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
sessionStorage = {}
@app.route("/", methods=['POST'])

def main():
    logging.info('Request: %r', request.json)
    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }
    handle_dialog(request.json, response)
    logging.info('Response: %r', response)
    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )

def handle_dialog(req, res, user_storage):
    user_storage = {}
    if req['session']['new']:
        for row in reader:
        res['response']['text'] = print(row)
        return

