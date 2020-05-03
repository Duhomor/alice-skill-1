# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging
import csv

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}

# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])

def main():
# Функция получает тело запроса и возвращает ответ.
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
    #temp = 'Расписание'
    #with open("eif.csv", "r", encoding="utf8") as file:
    #reader = csv.DictReader(file, delimiter=';')
    #for line in reader:
        #temp = temp + line["time"]
    
    if req['session']['new']:
        res['response']['text'] = 'Привет! Я бот ЯГТУ. Я могу показать расписание занятий для твоей группы. В какой группе ты учишься?'
        return
    
    if req['request']['original_utterance'].lower() in['эис-44']:
        res['response']['text'] = 'Расписание для ЭИС-44'
        return
    elif req['request']['original_utterance'].lower() in['эис-45']:
        res['response']['text'] = 'Расписание для ЭИС-45'
        return
    
    res['response']['text'] = 'Я не знаю такой группы. Попробуй ещё раз.'
    
