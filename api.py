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
    if req['session']['new']:
        res['response']['text'] = 'Привет! Я бот ЯГТУ. Я могу показать расписание занятий для твоей группы. В какой группе ты учишься?'
        return
    
    if req['request']['original_utterance'].lower() in['эмп-40', 'эмл-46', 'эмгх-46']:
        res['response']['text'] = 'ПН\n8.30-11.40 Учебная практика, Г-803\nПТ\n8.30-11.40 Учебная практика, Г-803'
        return
    
    if req['request']['original_utterance'].lower() in['ээ-47']:
        res['response']['text'] = 'ПН\n8.30-11.40 1-10н. Деловой англ.яз., пр.з.4ч, ч\н-Г-801, н\н-В-310\n1, 3, 5, 7,9н. Деловой англ.яз., пр.з.4ч, Г-735\nВТ\n12.20.15.30 1-10н. Инновационный менеджмент, лек., пр.з.4ч, В-202, со 2 н – В-217, с 7н лаб.4ч по п\гр, В-107 ст.пр.М.И.Маркин\nСР\n8.30-11.40 1-10н. Оценка и упр-ние стоимостью предп-тий, лек., пр.з.4ч, В-202 доц.А.В.Кольцова\n12.20-15.30 2,4,6н. Деловой англ.яз., пр.з.4ч, Г-735\nН\н с 3 по 9н. Оценка и упр-ние стоимостью предп-тий, пр.з.4ч, В-217\nЧТ\n8.30-11.40 2-10н. Бизнес-планирование и инвест.проект., лек.4ч, В-311, 9-10н – пр.з.4ч, В-107 ст.пр.М.А.Майорова\n12.20-15.30 1, 3-10н. Оценка и упр-ние стоимостью предпр, 1н – лек.4ч В-202, с 3н. лаб.4ч по п\гр, В-107\nПТ\n8.30-11.40 5-10н. Бизнес-планиро-вание и инвест.проект., лаб.4ч по п\гр, В-107'
        return
    
    if req['request']['original_utterance'].lower() in['эсм-42']:
        res['response']['text'] = ''
        return
    
    if req['request']['original_utterance'].lower() in['эук-43']:
        res['response']['text'] = ''
        return
    
    if req['request']['original_utterance'].lower() in['эис-44']:
        res['response']['text'] = ''
        return
    
    if req['request']['original_utterance'].lower() in['эис-45']:
        res['response']['text'] = ''
        return
    
    if req['request']['original_utterance'].lower() in['эпи-41']:
        res['response']['text'] = ''
        return
    
    if req['request']['original_utterance'].lower() in['эи-48']:
        res['response']['text'] = ''
        return
    
    if req['request']['original_utterance'].lower() in['спасибо', 'благодарю']:
        res['response']['text'] = 'Рада помочь.'   
        return
    
    if req['request']['original_utterance'].lower() in['помощь', 'помоги', 'help']:
        res['response']['text'] = 'Для того, чтобы узнать расписание занятий для своей группы, просто скажи мне её название, например, "ЭИС-44", а затем назови день недели, на который нужно найти расписание.'   
        return

    res['response']['text'] = 'К сожалению, я не знаю такой команды. Попробуй ещё раз или скажи "помощь" для того, чтобы запросить правила навыка.'
    
