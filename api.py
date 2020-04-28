from __future__ import unicode_literals
import json
import logging
from flask import Flask, request

from bs4 import BeautifulSoup as bs
import requests as req

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

def handle_dialog(req, res):
    if req['session']['new']:
        res['response']['text'] = 'Привет!'
        return
    if req['request']['original_utterance'].lower() in ['расписание']:
        res['response']['text'] = 'Факультет'
        return
