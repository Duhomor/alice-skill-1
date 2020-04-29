from __future__ import unicode_literals
import json
import logging
from flask import Flask, request
import csv

with open("ief.csv", "r", encoding = "utf8") as csvfile:
    data = csv.DictReader(csvfile, delimiter = ",", quotechar = " ")
    events = {x["event"]: [x["Часы"]] for x in data}

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
    for number in range(6)
    user_storage["event"] = events[number][1]
    user_storage["time"] = events[number][0]
    if req['session']['new']:
        res['response']['text'] = '{}'.format(user_storage["time"])' - {}'.format(user_storage["time"])
        return

