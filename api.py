# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging

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
    usstorage = {}
    if req['session']['new']:
        res['response']['text'] = 'Привет! Я бот ЯГТУ. Я могу показать расписание занятий для твоей группы. В какой группе ты учишься?'
        return
    
    if req['request']['original_utterance'].lower() in['эис-45']:
        userStorage['group'] = 'eis45',
        res['response']['text'] = 'Рассписание на какой день недели тебе нужно найти?'
        return
    
    if req['request']['original_utterance'].lower() in['понедельник']:
            res['response']['text'] = 'В какой группе ты учишься? {}'.format(usstorage['group'])
        return
    
    if req['request']['original_utterance'].lower() in['спасибо', 'благодарю']:
        res['response']['text'] = 'Рада помочь.'   
        return
    
    if req['request']['original_utterance'].lower() in['помощь', 'помоги', 'help']:
        res['response']['text'] = 'Для того, чтобы узнать расписание занятий для своей группы, просто скажи мне её название, например, "ЭИС-44", а затем назови день недели, на который нужно найти расписание.'   
        return

    res['response']['text'] = 'К сожалению, я не знаю такой команды. Попробуй ещё раз или скажи "помощь" для того, чтобы запросить правила навыка.'
    
