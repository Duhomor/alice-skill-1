from __future__ import unicode_literals
import json
import logging
from flask import Flask, request

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
        res['response']['text'] = 'Привет! Я бот'
        return
    if req['request']['original_utterance'].lower() in [
        'ладно',
    ]:
        # Пользователь согласился, прощаемся.
        res['response']['text'] = 'Слона можно найти на Яндекс.Маркете!'
        return
        if req['request']['original_utterance'].lower() in [
        'отлично',
    ]:
            res['response']['text'] = 'Тогда вот это'
        return

