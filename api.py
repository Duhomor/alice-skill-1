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
    storage = {}
    if req['session']['new']:
        res['response']['text'] = 'Привет! Я бот ЯГТУ. Я могу показать расписание занятий для твоей группы. В какой группе ты учишься?'
        return
        
    if req['request']['original_utterance'].lower() in['понедельник']:
        storage["day"] = 'Понедельник'
        return        
    elif req['request']['original_utterance'].lower() in['вторник']:
        storage["day"] = 'Вторник'
        return        
    elif req['request']['original_utterance'].lower() in['среда']:
        storage["day"] = 'Среда'
        return        
    elif req['request']['original_utterance'].lower() in['четверг']:
        storage["day"] = 'Четверг'
        return        
    elif req['request']['original_utterance'].lower() in['пятница']:
        storage["day"] = 'Пятница'
        return        
    elif req['request']['original_utterance'].lower() in['суббота']:
        storage["day"] = 'Суббота'
        return
        
    elif req['request']['original_utterance'].lower() in['эмп-40']:
        storage["group"] = 'эмп-40'
        return    
    elif req['request']['original_utterance'].lower() in['эпи-41']:
        storage["group"] = 'эпи-41'
        return    
    elif req['request']['original_utterance'].lower() in['эсм-42']:
        storage["group"] = 'эсм-42'
        return    
    elif req['request']['original_utterance'].lower() in['эук-43']:
        storage["group"] = 'эук-43'
        return    
    elif req['request']['original_utterance'].lower() in['эис-44']:
        storage["group"] = 'эис-44'
        return    
    elif req['request']['original_utterance'].lower() in['эис-45']:
        storage["group"] = 'эис-45'
        return    
    elif req['request']['original_utterance'].lower() in['эмл-46']:
        storage["group"] = 'эмл-46'
        return    
    elif req['request']['original_utterance'].lower() in['эмгх-46']:
        storage["group"] = 'эмгх-46'
        return
    elif req['request']['original_utterance'].lower() in['ээ-47']:
        storage["group"] = 'ээ-47'
        return
    elif req['request']['original_utterance'].lower() in['эи-48']:
        storage["group"] = 'эи-48'
        return
    
    res['response']['text'] = 'Я не знаю такой группы. Попробуй ещё раз.'
    
