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
    
    if req['request']['original_utterance'].lower() in['другая группа']:
        res['response']['text'] = 'Назови группу, для которой нужно найти расписание'   
        return
                
    if req['request']['original_utterance'].lower() in['эис-44']:
        storage["group"] = 'эис-44'
        res['response']['text'] = 'Расписание на какой день недели тебя интересует?'   
        return
                
    if req['request']['original_utterance'].lower() in['эук-43']:
        storage["group"] = 'эук-43'
        res['response']['text'] = 'Расписание на какой день недели тебя интересует?'   
        return
    
    if req['request']['original_utterance'].lower() in['понедельник']:
        storage["day"] = 'Понедельник'
        res['response']['text'] = '08.30-10.00 - 2-7н. Практика производственная, лек., пр.з. 4 ч., Г-606 \n10.10-11.40 \n11.40-12.20 \n12.20-13.50 - 2,7-10н. Всеобщее управление качеством, лек., пр.з. 4 ч., В-309 \n14.00-15.30 \n15.40-17.10 \n17.30-19.00'   
        return
    
    if req['request']['original_utterance'].lower() in['вторник']:
        storage["day"] = 'Вторник'
        res['response']['text'] = 'А'   
        return
    
    if req['request']['original_utterance'].lower() in['среда']:
        storage["day"] = 'Среда'
        res['response']['text'] = 'А'   
        return
    
    if req['request']['original_utterance'].lower() in['четверг']:
        storage["day"] = 'Четверг'
        res['response']['text'] = '08.30-10.00 - 3н. БЖД лаб. 4 ч. по п/гр, Г-721 \n10.10-11.40 - 5-6н. БЖД, пр.з. 4 ч., Г-903 \n11.40-12.20 \n12.20-13.50 - 2н. Защита интелл. собственности, пр.з. 4 ч., В-306 \n14.00-15.30 \n15.40-17.10 \n17.30-19.00'
        return
    
    if req['request']['original_utterance'].lower() in['пятница']
        storage["day"] = 'Пятница
        res['response']['text'] = 'А'   
        return
    
    if req['request']['original_utterance'].lower() in['суббота']:
        storage["day"] = 'Суббота'
        res['response']['text'] = 'А'   
        return
    
    if req['request']['original_utterance'].lower() in['воскресенье']:
        storage["day"] = 'воскресенье'
        res['response']['text'] = 'Этот день - выходной.'   
        return
    
    if req['request']['original_utterance'].lower() in['спасибо']:
        res['response']['text'] = 'Рада помочь.'   
        return
    
    if req['request']['original_utterance'].lower() in['помощь']:
        res['response']['text'] = 'Для того, чтобы узнать расписание занятий для своей группы, просто скажи мне её название, например, "ЭИС-44", а затем назови день недели, на который нужно найти расписание.'   
        return
    
    res['response']['text'] = 'К сожалению, я не знаю такой команды. Попробуй ещё раз или скажи "помощь" для того, чтобы запросить правила навыка.'
    
