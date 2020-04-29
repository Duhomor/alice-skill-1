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
        res['response']['text'] = 'Привет! Я бот Ярославского Политеха. Я могу показать расписание занятий для твоей группы. На каком факультете ты учишься?'
        return
    if req['request']['original_utterance'].lower() in [
        'Инженерно-экономический',
        'ИЭФ',
    ]:
        res['response']['text'] = 'Теперь мне нужно узнать, в какой ты группе'
        return
    if req['request']['original_utterance'].lower() in [
        'ЭИС-44',
        '44',
    ]:
        res['response']['text'] = 'Расписание на какой день недели тебя интересует?'
        return
    if req['request']['original_utterance'].lower() in [
        'Понедельник',
    ]:
        res['response']['text'] = 'Понедельник:\n8.30-10.00 -\n10.10-11.40 -\n11.40-12.20 -\n12.20-13.50 1-5 н. Защита интеллектуальной собственности, лек., доц. В.Г. Копыльцов, Г-909\n14.00-15.30 1-5 н. Защита интеллектуальной собственности, лек., доц. В.Г. Копыльцов, Г-909\n15.40-17.10 2-5 н. Защита интеллектуальной собственности, пр.з., Г-909\n17.30-19.00 2-5 н. Защита интеллектуальной собственности, пр.з., Г-909'
        return

