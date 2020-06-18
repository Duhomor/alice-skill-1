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
        res['response']['text'] = 'Привет! Я бот ЯГТУ. Я могу показать расписание занятий для твоей группы. В какой группе ты учишься?'
        return
    
    if req['request']['original_utterance'].lower() in['помощь', 'помоги', 'помочь', 'help', 'хэлп', 'подскажи', 'подсказка', 'подсказать', 'справка']:
        res['response']['text'] = 'Для того, чтобы узнать расписание занятий для своей группы, просто введи её название, например, "ЭИС-44". Чтобы закрыть навык, введи "Выход".'   
        return
    
    if req['request']['original_utterance'].lower() in['спасибо', 'спс', 'спасиб', 'спасибки', 'спасибочки', 'благодарю', 'мерси', 'сэнк ю', 'сэнкс', 'thank', 'thanks']:
        res['response']['text'] = 'Рад помочь.'   
        return
    
    if req['request']['original_utterance'].lower() in['выход', 'выйти', 'выйди', 'закрытие', 'закрыть', 'закрой', 'уход', 'уйти', 'уйди']:
        res['response']['text'] = 'До свидания.'  
        res['response']['end_session'] = True 
        return
    
    if req['request']['original_utterance'].lower() in['эм-10']:
        res['response']['text'] = 'ПН\n10.10-11.40 Н\н с 3 по 13н. Орг-ция предпр. деят-сти., Г-801\n11.50-13.50 Физ.культура, на 2н лек., акт. зал, с 3н пр.з.\n14.00-15.30 2-13н. История, лек., Б–122\n15.40-17.10 2-17н. История, пр.з., А-408\nВТ\n12.20-13.50 2-17н. (кр.14н) Математика, пр.з., Б-224\nСР\n8.30-11.40 4-17н. Мат.методы и модели в менеджменте, лаб.4ч по п\гр, Г-812\n11.50-13.50 Физ.культура, со 2н пр.з.\n14.00-15.30 2-15н. Мат.методы и модели в менеджменте, лек., А-414\nЧТ\n8.30-11.40 Ч\н со 2 по 16н. Англ.яз., пр.з.4ч, Г-812\n Н\н с 7 по 17н. Эконом.теор., пр.з.4ч, В-218\n12.20-15.30 Н\н с 7 по 17н. Орг-ция предпр.деят-сти, лаб.4ч по п\гр, Г-625\nПТ\n8.30-10.00 5-6н. Математика, пр.з., Б-224\n10.10-11.40 Ч\н со 2 по 16н. Математика, пр.з., Б-224\nН\н с 3 по 17н. Орг-ция предпр.деят-сти, пр.з., Г-812\n12.20-13.50 2-15н. (кр.13н) Математика (мат.анализ), лек., Б-203\n17н. Эконом.теор. (макроэкономика), лек., Б-203\n14.00-15.30 2-17н. (кр.13н) Эконом.теор. (макроэкономика), лек., Б-203\n15.40-19.00 2-10н. Англ.яз., пр.з.4ч, Г-801'
        return
    
    if req['request']['original_utterance'].lower() in['ээ-19']:
        res['response']['text'] = 'ПН\n10.10-11.40 Н\н с 3 по 13н. Орг-ция предпр.деят-сти, Г-801\n11.50-13.50 Физ.культура, на 2н лек., акт.зал\n14.00-15.30 2-13н. История, Б-122\nВТ\n8.30-10.00 Ч\н с 8 по 16, 15, 17н. (кр.10н.) История развит.предпр., пр.з.4ч, В-217\n10.10-11.40 Ч\н со 2 по 8н. История развит.предпринимат., В-217\n14.00-15.30 2-17н. (кр.14н) Математика, пр.з., Б-224\n15.40-19.00 13,15н. Англ.яз., пр.з.4ч, Г-812\nСР\n10.10-11.40 2-14н. Педагогика проф.деятельности, лек., пр.з., В-216\n11.50-13.50 Физ.культура\n14.00-15.30 4-17н. Регион.экономика, лек., пр.з., А-408\n15.40-19.00 с 4 по 16н. Регион.экономика, А-408\nЧТ\n8.30-11.40 Ч\н с 6 по 16н. Макроэкономика, пр.з.4ч, В-218\n12.20-15.30 2-17н. Англ.яз., пр.з.4ч по п\гр, Г-812\nПТ\n8.30-10.00 2-4н. Мат.анализ, пр.з., Б-224\n10.10-11.40 Н\н с 3 по 17н. Мат.анализ, пр.з., Б-224\n12.20-13.50 2-15н. (кр.13н) Математика (мат.анализ), Б-203\n14.00-15.30 2-17н. (кр.13н) Эконом.теория (макроэкономика), Б-203\n15.40-17.10 4,6,8н. Регион.экономика, лек., пр.з., А-408'
        return
    
    if req['request']['original_utterance'].lower() in['эи-18']:
        res['response']['text'] = 'ПН\n8.30-11.40 2-17н. Немец.яз., пр.з.4ч, по п\гр\n11.50-13.50 Физ.культура, на 2н лек., акт.зал\n14.00-15.30 2-13н. История, лек., Б-122\nВТ\n8.30-11.40 2-17н. Немец.язык, пр.з.4ч по п\гр, Г-726\n12.20-13.50 2-11н. Информатика, Г-611\n14.00-15.30 2-11н. Технолог.программирования, Г-611\n15.40-17.10 2-10н. Мат.анализ, пр.з., Б-224\nСР\n8.30-11.40\n2-17н. Немец.язык, пр.з.4ч по п\гр, Г-726\n2-17н. Информатика, лаб.4ч по п\гр, Г-625\n11.50-13.50 Физ.культура\n14.00-15.30 2-7н. Экономика предпр., лек., пр.з.4ч, В-202\nЧТ\n8.30-11.40 2-17н. Немец.язык, пр.з.4ч по п\гр, Г-726\n12.20-15.30 2-5н. Экономика предпр., лек., пр.з.4ч, В-202, на 3н В-304\n6-17н. Налоги и налогообложение, лек., пр.з.4ч, В-202\nПТ\n10.10-11.40 5-17н. История, пр.з., А-408\n12.20-13.50 2-15н. (кр.13н) Математика (мат.анализ), Б-203\n14.00-15.30 2-17н. Мат.анализ, пр.з., Б-224\n15.40-19.00 2-12н. Технолог.программирования, лаб.4ч по п\гр, Г-625\n2-7н. Немец.язык, пр.з.4ч по п\гр, Г-726\n14-17н. Информатика, лаб.4ч по п\гр, Г-625'
        return
    
    if req['request']['original_utterance'].lower() in['эсм-12']:
        res['response']['text'] = 'ПН\n8.30-10.00 5-11н. Материаловедение, пр.з., А-118, 139\n12н. Материаловедение, лаб.4ч по п\гр, А-118, 139\n13,17н. Англ.яз., пр.з.4ч, А-414\n10.10-11.40 2-11н. Материаловедение, А-414\n11.50-13.50 Физ.культура, на 2н лек., акт.зал\n14.00-15.30 2-13н. История, Б-122\nВТ\n8.30\n11.40 5-17н. История, пр.з., А-408\n8-17н. Математика, пр.з., А-409\n12.20-13.50 2-17н. (кр.14н.) Теор.механика, лек., пр.з.4ч, А-216\nСР\n8.30-10.00 2-17н. Инж.и компьютерная графика, лаб.2ч, А-211\n10.10-11.40 2-17н. Математика, пр.з., А-408\n11.50-13.50 Физ.культура\nЧТ\n8.30-10.00 Н\н с 3 по 13н. Химия, лек., пр.з., Б-305 А\n14-17н. Химия, лаб.4ч, Б-305\n10.10-11.40 2-13н. Теор.механика, лек., пр.з., А-216\n12.20-13.50 2-12н. Физика, пр.з., А-236\n14.00-15.30 2-12н. Англ.яз., пр.з.4ч по п\гр, А-408\nПТ\n8.30-11.40 Ч\н с 4 по 16н. Физика, лаб.4ч, А-328, 329\nН\н с 3 по 17н. Материаловедение, лаб.4ч по п\гр, А-118, 139\n12.20-13-50 2-11н. Физика, А-414\n12-17н. Англ.яз., пр.з.4ч, по п\гр, А-415\n14.00-15.30 2-11н. Математика, А-414'
        return
    
    if req['request']['original_utterance'].lower() in['эук-13']:
        res['response']['text'] = 'ПН\n10.10-11.40 2-11н. Материаловедение, А-414\n11.50-13.50 Физ.культура, на 2н лек., акт.зал\n14.00-15.30 2-13н. История, Б-122\n15.30-19.00 5-13н. Технология и орг-ция производства продукции и услуг, лаб.4ч по п\гр, А-135, 141\nВТ\n8.30-10.10 8-17н. Математика, пр.з., А-409\n10.10-11.40 5-17н. История, пр.з., А-408\n12.20-13.50 2-17н. Мат.методы и модели в упр-нии качеством, пр.з., Г-812\nСР\n8.30-10.00 2-17н. Математика, пр.з., А-408\n10.00-11.40 2-17н. Инж.и компьютерная графика, лаб.2ч, А-211\n11.50-13.50 Физ.культура\n14.00-15.30 2-15н. Мат.методы и модели в упр-нии качеством, А-414\nЧТ\n10.10-11.40 2-12н. Физика, пр.з., А-236\n13,15,17н. . Мат.методы и модели в упр-нии качеством, пр.з., Г-801\n12.20-15.30 Н\н с 3 по 13н. Химия, пр.з.2ч, Б-305А\nЧ\н со 2 по 16н. Англ.яз., пр.з.4ч, Г-735\nПТ\n8.30-11.40 Н\н с 3 по 17н. Физика, лаб.4ч, А-328, 329\n12.20-13.50 2-11н. Физика, А-414\n14.00-15.30 2-11н. Математика, А-414\n15.40-19.00 2-10н. Немец.язык, пр.з.4ч, Г-812\n11н. Англ.яз., пр.з.4ч, Г-735'
        return
    
    if req['request']['original_utterance'].lower() in['эис-14']:
        res['response']['text'] = 'ПН\n8.30-10.00 Н\н с 3 по 11н. Основы программирования, А-315\n11.50-13.50 Физ.культура, на 2н лек, акт.зал\n14.00-19.00 2-17н. ОС, лаб.4ч по п\гр, Г-207\n5-13н. Электроника и схемотехника, лаб.4ч по п\гр, В-404, 407\nВТ\n8.30-11.40 3-17н. Основы программирования, лаб.4ч по п\гр, Г-630\n2-15н. Англ.яз, пр.з.4ч по п\гр, Г-725\n5-17н. Арх-ра инф.систем, лаб.4ч по п\гр, Г-507\n15.40-17.10 Н\н с 3 по 17, 12, 16н. Математика, пр.з., Б-226\nСР\n8.30-11.40 Ч\н со 2 по 16 н. История, А-315\n11.50-13.50 Физ.культура\n14.00-15.30 2,4,12,14н. Электроника и схемотехника, А-315\n3,5-11н. Арх-ра инф.систем, А-315\n15.40-19.00 Н\н с 3 по 17н. ОС, лаб.4ч по п\гр, Г-207\nЧТ\n12.20-15.30 2-17н. Англ.яз., пр.з.4ч, по п\гр, Г-725\nПТ\n8.30-10.00 2-4н.История, пр.з., Г-808\n5-17н. Основы менедж-та, пр.з., Г-808\n10.00-13.50 2-16н. Математика, А-315\n14.00-15.30 2-16н. Основы менедж-та, А-315\n15.40-17.10 4н. История, пр.з., А-416\nСБ\n8.30-11.40 2,4,8н. Электроника и схемотехника, А-315\n12.20-15.30 17н. Арх-ра инф.систем, А-315'
        return
    
    if req['request']['original_utterance'].lower() in['эис-15']:
        res['response']['text'] = 'ПН\n8.30-10.00 Н\н с 3 по 11н. Основы программир., А-315\n11.50-13.50 Физ.культура, на 2н лек., акт.зал\n14.00-19.00 2-17н. ОС, лаб.4ч по п\гр, Г-207\nВТ\n8.30-11.40 2-17н. Электроника и схемотехника, лаб.4ч по п\гр, В-404, 407\n12.20-15.30 2-17н. ОС, лаб.4ч по п\гр, Г-207\n3-17н. Основы программир., лаб.4ч по п\гр, Г-633\nСР\n10.10-11.40 Ч\н со 2 по 16 н. История, А-315\n11.50-13.50 Физ.культура\n14.00-15.30 2,4,12,14н. Электроника и схемотехника, А-315\n3,5-11н. Арх-ра инф.систем, А-315\n15.40-17.10 2-17н. Математика, пр.з., Б-226\nЧТ\n8.30-11.40 2-17н. Англ.яз., пр.з.4ч, по п\гр, Г-735\n12.20-15.30 4-15н. Основы менедж-та, пр.з., Г-808\n4-15н. История, пр.з, А-414\n15.40-19.00 7-15н. Математика, пр.з., Б-22\nПТ\n8.30-11.40 2-16н. Англ.яз., пр.з.4ч, 2 п\гр, Г-728\n10.00-13.50 2-16н. Математика, А-315\n14.00-15.30 2-16н. Основы менедж-та, А-315\n15.40-19.00 2-17н. Немец.язык, Г-812\n2-17н. Франц.язык, Г-813\nСБ\n8.30-11.40 Н\н с 3 по 11н. ОС, лаб.4ч по п\гр, Г-207\n12.20-15.30 17н. Арх-ра инф.систем, А-315'
        return
    
    if req['request']['original_utterance'].lower() in['эис-16']:
        res['response']['text'] = 'ПН\n8.30-11.40 Н\н с 3 по 11н. Основы программирования, А-315\n11.50-13.50 Физ.культура, на 2н. лек., акт.зал\n14.00-15.30 2-17н. ОС, А-315\n15.40-19.00 2-17н. Англ.яз., пр.з.4ч, Г-812\nВТ\n8.30-11.40 2-17н. ОС, лаб.4ч по п\гр, Г-207\n3-17н. Основы программирования, лаб.4ч по п\гр, Г-633\n12.20-13.50 4н. История, пр.з., А-417\nСР\n8.10-11.40 Ч\н со 2 по 16н. История, А-315\nН\н с 3 по 17н. Математика, пр.з., Б-226\n11.50-13.50 Физ.культура\n14.00-15.30 3,5-11н. Арх-ра инф.систем, А-315\n15.40-19.00 6-17н. Арх-ра инф.систем, лаб.4ч по п\гр, Г-507\n12.20-15.30 2-17н. Англ.яз., пр.з.4ч по п\гр, А-409\n15.30-17.10 5-6н. Математика, пр.з., Б-226\nПТ\n8.30-10.00 2-17н. Математика, пр.з., Б-226\n10.10-11.40 2-4н. История, пр.з., Г-808\n12.20-13.50 2-16н. Математика, А-315\n14.00-15.30 2-16н. Основы менедж-та, А-315\n15.40-19.00 2-17н. Нем.язык, пр.з.4ч, Г-812\nСБ\n8.30-11.40 2, 4, 8н. Электроника и схемотехника, А-315\n12.20-15.30 17н. Арх-ра инф.систем, А-315\nН\н с 3 по 11н. ОС, лаб.4ч по п\гр, Г-207'
        return
    
    if req['request']['original_utterance'].lower() in['эис-17']:
        res['response']['text'] = 'ПН\n8.30-11.40 Н\н с 3 по 11н. Основы программирования, А-315\nЧ\н со 2 по 16, 13, 17н. Англ.яз., по п\гр, Г-735\n11.50-13.50 Физ.культура, на 2н. лек., акт.зал\n14.00-15.30 2-17н. ОС, А-315\nВТ\n8.30-11.40 2-15н. Математика, пр.з., Б-224\n12.20-13.50 5-17н. Основы менеджмента, пр.з., А-416\n14.00-15.20 4н. История, пр.з., А-417\nСР\n8.30-11.40 Н\н с 3 по 17н. Англ.яз., по п\гр, Г-735\n10.10-11.40 Ч\н со 2 по 16н. История, А-315\n11.50-13.50 Физ.культура\n14.00-15.30 3,5-11н. Арх-ра инф.систем, А-315\n2,4,12,14н. Электроника и схемотехника, А-315\n15.40-19.00 2,6,10,14н. ОС, лаб. по п\гр, Г-207\nЧТ\n8.30-11.40 2-17н. ОС, лаб. по п\гр, Г-207\n11.40-12.20 2-17н. Электроника и схемотехника, лаб. по п\гр, В-404, 407\nПТ\n8.30-11.40 2-14н. Англ.яз., по п\гр, Г-735\n12.20-13.50 2-16н. Математика, А-315\n14.00-15.30 2-16н. Основы менедж-та, А-315\n15.40-19.00 2-17н. Нем.язык, пр.з., Г-812\nСБ\n8.30-11.40 2, 4, 8н. Электроника и схемотехника, А-315\n12.20-15.30 17н. Арх-ра инф.систем, А-315'
        return
    
    if req['request']['original_utterance'].lower() in['эис-17а']:
        res['response']['text'] = 'ПН\n8.30-11.40 Н\н с 3 по 11н. Основы программирования, А-315\nЧ\н со 2 по 12н. Англ.яз., по п\гр, А-408\n11.50-13.50 Физ.культура, на 2н. лек., акт.зал\n14.00-15.30 2-17н. ОС, А-315\nВТ\n8.30-11.40 2-15н. Математика, пр.з., Б-224\n12.20-13.50 5-17н. История, пр.з., А-417\nСР\n8.30-11.40 Н\н с 3 по 17н. Англ.яз., по п\гр А-413\n10.10-11.40 Ч\н со 2 по 16н. История, А-315\n11.50-13.50 Физ.культура\n14.00-15.30 3,5-11н. Арх-ра инф.систем, А-315\n15.40-19.00 4,8,12,16н. ОС, лаб. по п\гр, Г-207\nЧТ\n8.30-11.40 2-17н. Электроника и схемотехника, лаб. по п\гр, В-404, 407\n6-17н. Арх-ра инф.систем, лаб. по п\гр, Г-507\n12.20-15.30 2-17н. ОС, лаб. по п\гр, Г-207\n4-17н. Основы программирования, лаб. по п\гр, Г-633\nПТ\n8.30-11.40 2-17н. Англ.яз., по п\гр, В-305\n12.20-13.50 2-16н. Математика, А-315\n14.00-15.30 2-16н. Основы менедж-та, А-315\n15.40-19.00 2-17н. Нем.язык, пр.з., Г-812\nСБ\n8.30-11.40 2, 4, 8н. Электроника и схемотехника, А-315\n12.20-15.30 17н. Арх-ра инф.систем, А-315'
        return
    
    if req['request']['original_utterance'].lower() in['эпи-11']:
        res['response']['text'] = 'ПН\n10.10-11.40 2-12н. Электроника и схемотехника, Г-506\n11.50-13.50 Физкультура, на 2н. лек., акт.зал\n14.00-15.30 2-17н. Маш-завис языки прогр-ния, Г-506\n15.40-19.00 2-17н. Электроника и схемотехника, лаб. по п\гр, Г-507\n5-10н. Проектн.практикум, лаб. по п\гр, Г-630\nВТ\n8.30-11.40 2-4н. Электроника и схемотехника, лаб. по п\гр, Г-507\n2-15н. Англ.яз., по п\гр, Г-812\n12.20-15.30 2-17н. Проектный практикум, лаб. по п\гр, Г-630\n2-17н. Англ.яз., по п\гр, Г-727, с 5н. – Г-803\nСР\n10.10-11.40 Н\н с 3 по 17н. История, А-414\nЧ\н со 2 по 14н. Математика, пр.з., А-414\n11.50-13.50 Физкультура\n14.00-15.30 2-15н. ОС, Г-306\n15.40-17.10 4-17н. История, пр.з., Г-801\nЧТ\n8.30-11.40 2-15н. Основы менедж-та, Г-803\n12.20-15.30 2-15н. Математика, А-414\nПТ\n8.30-11.40 2-17н. ОС, лаб. по п\гр, Г-207\n12.20-15.30 2-6н. Электроника и схемотехника, лаб. по п\гр, Г-630\n15.40-19.00 2-7н. (кр.4н.). Маш-завис языки прогр-ния, лаб. по п\гр, Б-223а\nСБ\n8.30-11.40 Ч\н со 2 по 10н. ОС, лаб. по п\гр, Г-207'
        return
    
    if req['request']['original_utterance'].lower() in['эпи-11а']:
        res['response']['text'] = 'ПН\n10.10-11.40 2-12н. Электроника и схемотехника, Г-506\n11.50-13.50 Физкультура, на 2н. лек., акт.зал\n14.00-15.30 2-17н. Машинно-зависимые языки программирования, Г-506\n15.40-19.00 5-10н. Проектн.практикум, лаб. по п\гр, Г-630\nВТ\n12.20-15.30 2-4н. Электроника и схемотехника, лаб. по п\гр, Г-507\n15.30-19.00 2-17н. Проектный практикум, лаб. по п\гр, Г-630\nСР\n8.30-10.00 со 2 по 17н. Математика, пр.з., Б-226\n10.10-11.40 Н\н с 3 по 17н. История, А-414\nЧ\н со 2 по 16н. Математика, пр.з., Б-226\n11.50-13.50 Физкультура\n14.00-15.30 2-15н. ОС, Г-306\n15.40-19.00 3н. Маш-завис языки прогр-ния, лаб. по п\гр, Г-630\nЧТ\n8.30-10.00 2-17н. (кр.13-15н) Англ.яз., по п\гр, А-417\n10.10-11.40 2-15н. Основы менеджмента, Г-803\n16-17н. Англ.яз., по п\гр, А-417\n12.20-13.50 2-15н. Математика, А-414\n14.00-15.30 4-15н. Основы менедж-та, пр.з., Г-808\nПТ\n10.10-11.40 5-17н. История, пр.з., А-409\n15.30-19.00 2-17н. Немец. язык, Г-812\nСБ\n12.20-15.30 Ч\н со 2 по 10н. ОС, лаб. по п\гр, Г-207'
        return
    
    if req['request']['original_utterance'].lower() in['эмп-20', 'эмл-20']:
        res['response']['text'] = 'ПН\n8.30-10.00 Н\н с 3 по 17н. Статистика, Г-506\n10.10-11.40 Физкультура\n12.20-15.30 2,3,8-17н. Инф.технологии в менедж-те, пр.з., с 8н. лаб. по п\гр, Г-625\n5-17н. Статистика, лаб. по п\гр, Г-630\n15.40-19.00 3-12н. Упр-ние затратами, лаб. по п\гр, Г-633\nВТ\n8.30-10.00 3,4н. Маркетинг, лаб. по п\гр, Б-223А\n10.10-11.40 2н. Финансы и кредит, Г-613\n12.20-13.50 2н. Упр-ние затратами, Г-506\n6-17н. Маркетинг, пр.з., Г-909\n14.00-15.30 6-8н. Статистика, пр.з., Г-608\n9-17н. Правоведение, пр.з., А-407\nСР\n8.30-10.00 Н\н с 3 по 17н. Маркетинг, лаб. по п\гр, Г-633\n10.10-11.40 Ч\н со 2 по 12н. Упр-ние затратами, Г-506\n12.20-13.50 Н\н с 3 по 17, 14,16н. Маркетинг, А-315\n14.00-15.30 Физкультура\n15.40-17.10 2н. Маркетинг, А-414\nЧТ\n12.20-13.50 2-17н. Финансы и кредит, Г-611\n14.00-15.30 2-17н. Упр-ние инновац., Г-801\n15.40-19.00 Ч\н со 2 по 12н. Финансы и кредит, лаб. по п\гр, Г-633\nПТ\n8.30-10.00 8-9н. Упр-ние затратами, Г-506\n10.10-11.40 2-9н. Упр-ние затратами, Г-506\n12.20-15.30 2-10н. Ин. язык'
        return
    
    if req['request']['original_utterance'].lower() in['эмгх-20']:
        res['response']['text'] = 'ПН\n8.30-10.00 Н\н с 3 по 17н. Статистика, Г-506\n10.10-11.40 Физкультура\n12.20-15.30 2,3,8-17н. Инф.технологии в менедж-те, пр.з., с 8н. лаб. по п\гр, Г-625\n15.40-19.00 3-12н. Упр-ние затратами, лаб. по п\гр, Г-633\nВТ\n8.30-10.00 3,4н. Маркетинг, лаб. по п\гр, Б-223А\n10.10-11.40 2н. Финансы и кредит, Г-613\n12.20-13.50 2н. Упр-ние затратами, Г-506\n6-17н. Маркетинг, пр.з., Г-909\n14.00-15.30 6-8н. Статистика, пр.з., Г-608\n9-17н. Правоведение, пр.з., А-407\nСР\n8.30-10.00 Н\н с 3 по 17н. Маркетинг, лаб. по п\гр, Г-633\n10.10-11.40 Ч\н со 2 по 12н. Упр-ние затратами, Г-506\n12.20-13.50 Н\н с 3 по 17, 14,16н. Маркетинг, А-315\n14.00-15.30 Физкультура\n15.40-17.10 2н. Маркетинг, А-414\nЧТ\n12.20-13.50 2-17н. Финансы и кредит, Г-611\n14.00-15.30 2-17н. Гос.и муниц.упр-ние город.собст-стью, Г-806\n15.40-19.00 Ч\н со 2 по 12н. Финансы и кредит, лаб. по п\гр, Г-633\nПТ\n8.30-10.00 8-9н. Упр-ние затратами, Г-506\n10.10-11.40 2-9н. Упр-ние затратами, Г-506\n12.20-15.30 2-10н. Ин. язык'
        return
    
    if req['request']['original_utterance'].lower() in['ээ-28']:
        res['response']['text'] = 'ПН\n8.30-10.00 Н\н с 3 по 17н. Статистика, Г-506\n10.10-11.40 Физкультура\n12.20-15.30 3н. Маркетинг, пр.з., А-409\n5-17н. Маркетинг, лаб. по п\гр, Г-633\nВТ\n10.10-11.40 2-11н. Финансы, В-218\n12.20-15.30 6-8н. Статистика, пр.з., Г-608\n2-5, 9-12н. Информац.технологии в экономике, пр.з., Г-608\n15.40-19.00 5,7н. Методы оптим.решений, лаб. по п\гр, Г-625\n4,6-17н. Информац.технологии в экономике, Б-223А\nСР\n8.30-11.40 Н\н с 3 по 17н. Статистика, лаб. по п\гр, Г-630\nЧ\н со 2 по 16н. Англ.яз., пр.з., Г-735\n12.20-13.50 Н\н с 3 по 17, 14,16н. Маркетинг, А-315\n14.00-15.30 Физкультура\n15.40-17.10 2н. Маркетинг, А-414\nЧТ\n8.30-11.40 Ч\н со 2 по 16н. Экономика и управление качеством, по п\гр, В-217\nН\н с 3 по 17н. Финансы, по п\гр, В-107\n12.20-15.30 2-17н. Методы оптим.решений, Г-608\nПТ\n8.30-11.40 2-10н. Экономика недвижимости, В-218\n15н. Англ.яз., пр.з., Г-735\n16-17н. Методы оптим.решений, Г-608\n12.20-15.30 2-10н. Немец.язык, Г-812\nСБ\n12.20-15.30 2-10н. Франц.язык, пр.з., Г-812'
        return
    
    if req['request']['original_utterance'].lower() in['эи-28']:
        res['response']['text'] = 'ПН\n8.30-10.00 Н\н с 3 по 17н. Статистика, Г-506\n10.10-11.40 Физкультура\n12.20-15.30 Н\н с 3 по 17н. Информац.технологии упр-ния предпр., лаб., Г-207\nВТ\n12.20-13.50 6-8н. Статистика, пр.з., Г-608\nСР\n8.30-10.00 Н\н с 3 по 17н. Статистика, лаб. по п\гр, Г-630\n12.20-13.50 2-17н. Немец.язык, пр.з., Г-726\n14.00-15.30 Физкультура\nЧТ\n8.30-11.40 2-14н. Бух.учёт, по п\гр, В-201\n12.20-15.30 Ч\н со 2 по 12н. Бух.учёт, В-204 А\nН\н с 3 по 17н. Инф.технологии упр-ния предпр., Г-506\nПТ\n8.30-11.40 2-14н. Немец. язык, пр.з., Г-726\n12.20-15.30 2,17н. Статистика, лаб. по п\гр, Г-633'
        return
    
    if req['request']['original_utterance'].lower() in['эсм-22']:
        res['response']['text'] = 'ПН\n8.30-10.00 2-17н. Физика, А-414\n10.10-11.40 Физкультура\n12.20-15.40 Н\н с 3 по 13н. Аккредитация органов по сертиф-ции и испыт.лаборатор., А-137\nЧ\н с 8 по 16н. Физика, лаб., А-322\nВТ\n8.30-10.00 Н\н с 3 по 15н. Общая теория измерений, А-137\n10.10-11.40 2-15н. Теория машин и механизмов, Г-912\n12.20-15.30 Н\н с 3 по 15н. Норм-но-метод. база стандартизации, пр.з., Г-337\n17н. Англ.яз., пр.з., Г-735\nСР\n8.30-11.40 Ч\н с 4 по 12н. Сопромат, А-216\n12.20-13.50 Ч\н со 2 по 12н. Правоведение, А-315\n14.00-15.30 Физкультура\n15.40-17.10 3-16н. Норм-но-методическая база стандартизации, А-414\nЧТ\n8.30-10.00 Ч\н с 4 по 16н. Физика, пр.з., А-326\n10.10-11.40 Ч\н со 2 по 16н. Правоведение, пр.з., Г-809\n12.20-15.30 Ч\н со 2 по 16н. Физ.основы измерений и эталоны, пр.з., А-408\nН\н с 3 по 17н. Англ.яз., Г-735\nПТ\n8.30-10.00 Ч\н со 2 по 16н. Физ.основы измерений и эталоны, А-315\n10.10-11.40 Ч\н с 4 по 16н. Общая теория измерений, Г-337\n12.20-15.30 2-10н. Ин.Язык, А-415\nСБ\n2-10н. Франц.язык, пр.з., Г-812'
        return
    
    if req['request']['original_utterance'].lower() in['эук-23']:
        res['response']['text'] = 'ПН\n8.30-10.00 Ч\н со 2 по 17н. Физика, А-414\n10.10-11.40 Физкультура\n12.20-15.30 Н\н с 5 по 13н. Физика, лаб., А-322\nВТ\n10.10-11.40 Ч\н со 2 по 12н. Метрология и сертификация, пр.з., А-414\n12.20-13.50 2,4н. Англ.яз., пр.з., Г-735\n9-17н. Правоведение, пр.з., А-407\n14.00-15.30 9-17н. Маркетинг, пр.з., Г-909\nСР\n8.30-11.40 Ч\н с 4 по 16н. Норм-но-метод.база стандартизации, пр.з., Г-337\nН\н с 5 по 15н. Физ.основы измерений, лаб. по п\гр, А-326\n12.20-13.50 Ч\н со 2 по 12н. Правоведение, А-315\nН\н с 3 по 17н. Маркетинг, А-315\n14.00-15.30 Физкультура\n15.40-17.10 3-16н. Норм-но-методическая база стандартизации, А-414\nЧТ\n8.30-10.00 Н\н с 3 по 15н. Физика, пр.з., А-326\nЧ\н со 2 по 16н. Метрология, пр.з., Г-809\n10.10-11.40 2-16н. Метрология и сертификация, Г-611\n12.20-15.30 2-17н. Метрология и сертификация, лаб. по п\гр, А-225\n8-17н. Маркетинг, лаб. по п\гр, А-211\nПТ\n8.30-11.40 Ч\н со 2 по 16н. Физ.основы измерений и эталоны, А-315\n12.20-15.30 Ин.Язык, Г-909'
        return
    
    if req['request']['original_utterance'].lower() in['эис-24']:
        res['response']['text'] = 'ПН\n10.10-11.40 Физкультура\n12.20-15.30 2-17н. Англ.яз., по п\гр, Г-725\n2-17н. Информац.технологии, лаб. по п\гр, А-225\n15.40-19.00 2-17н. Технологии программирования, лаб. по п\гр, Г-625\nВТ\n8.30-15.30 2-17н. Англ.яз., по п\гр, Г-725\n12.20-15.30 2-9н. Информац.технологии, лаб. по п\гр, А-225\nСР\n10.10-11.40 Ч\н со 2 по 16н. Правоведение, пр.з., А-409\n12.20-13.50 2-17н. Технологии программирования, А-332\n14.00-15.30 Физкультура\n15.40-17.10 Правоведение, А-315\nЧТ\n8.30-11.40 2-17н. Англ.яз., по п\гр, Г-725\n2-6н. Инфок.системы и сети, лаб. по п\гр, Г-501\n12-17н. Упр-ние данными, лаб. по п\гр, Е-14В\n12.20-13.50 Ч\н со 2 по 16н. Информац.технологии, А-315\nН\н с 3 по 15н. Управление данными, А-315\n14.00-15.30 2-11н. Инфок.системы и сети, А-315\n12, 14н. Информационные технологии, А-315\n13, 15, 16н. Управление данными, А-315\nПТ\n8.30-11.40 2-17н. Инфок.системы и сети, лаб. по п\гр, Г-501\n2-16н. Технология программирования, лаб. по п\гр, Г-625\nСБ\n2-17н. Управление данными, лаб. по п\гр, Е-14В'
        return
    
    if req['request']['original_utterance'].lower() in['эис-25']:
        res['response']['text'] = ''
        return
    
    if req['request']['original_utterance'].lower() in['эис-26']:
        res['response']['text'] = ''
        return
    
    if req['request']['original_utterance'].lower() in['эис-27']:
        res['response']['text'] = ''
        return
    
    if req['request']['original_utterance'].lower() in['эпи-21']:
        res['response']['text'] = ''
        return
    
    if req['request']['original_utterance'].lower() in['эмп-40', 'эмл-46', 'эмгх-46']:
        res['response']['text'] = 'ПН\n8.30-11.40 Учебная практика, Г-803\nПТ\n8.30-11.40 Учебная практика, Г-803'
        return
    
    if req['request']['original_utterance'].lower() in['ээ-47']:
        res['response']['text'] = 'ПН\n8.30-11.40 1-10н. Деловой англ.яз., пр.з.4ч, ч\н-Г-801, н\н-В-310\n1, 3, 5, 7,9н. Деловой англ.яз., пр.з.4ч, Г-735\nВТ\n12.20.15.30 1-10н. Инновационный менеджмент, лек., пр.з.4ч, В-202, со 2 н – В-217, с 7н лаб.4ч по п\гр, В-107 ст.пр.М.И.Маркин\nСР\n8.30-11.40 1-10н. Оценка и упр-ние стоимостью предп-тий, лек., пр.з.4ч, В-202 доц.А.В.Кольцова\n12.20-15.30 2,4,6н. Деловой англ.яз., пр.з.4ч, Г-735\nН\н с 3 по 9н. Оценка и упр-ние стоимостью предп-тий, пр.з.4ч, В-217\nЧТ\n8.30-11.40 2-10н. Бизнес-планирование и инвест.проект., лек.4ч, В-311, 9-10н – пр.з.4ч, В-107 ст.пр.М.А.Майорова\n12.20-15.30 1, 3-10н. Оценка и упр-ние стоимостью предпр, 1н – лек.4ч В-202, с 3н. лаб.4ч по п\гр, В-107\nПТ\n8.30-11.40 5-10н. Бизнес-планиро-вание и инвест.проект., лаб.4ч по п\гр, В-107'
        return
    
    if req['request']['original_utterance'].lower() in['эсм-42']:
        res['response']['text'] = 'ПН\n8.30-11.40 1-10н. Разработка и внедрение систем менеджмента и TQM, лек., пр.з., лаб.4ч по п\гр, Г-337, со 2 н – А-137 доц.С.А.Соловьева\n12.20-15.30 3-10н. Методы и ср-ва измерений, испытан.и контроля, лаб.4ч по п\гр, А-218\nВТ\n8.30-11.40 1-10н. Эконом.и орг-ция пр-ва, лек., пр.з.4ч, доц.Ю.В.Бекренев, В-312\n12.20-15.30 2-10н. Эконом.и орг-ция пр-ва, лаб.4с по п\гр, В-218\nСР\n8.30-11.40 4,6,8н. Разработка и внедрение систем менеджмента и TQM, лаб.4ч, Г-337\n12.20-15.30 1-10н. Орг-ция и технология испытаний, лек., пр.з., 4ч, Г-337, асс.Е.О.Побегалова\nЧТ\n8.30-11.40 2-9н. Методы и ср-ва измерен., и контроля, лек., пр.з.4ч, А-137 ст.пр.Е.П.Кондратьева\n10н. Автоматизация измерен., испытан., лаб.4ч по п\гр, А-218\n12.20-15.30 2-10н. Автоматизация измерен., испытан.и контроля, лек., пр.з.4ч, А-137, с 8н лаб.4ч по п\гр, А-218\nПТ\n12.20-15.30 1-10н. Орг-ция и технология испытан., лаб.4ч по п\гр, А-118, 218, на 1 и 2н. – лек., пр.з.4ч, Г-337\n15.40-19.00 10н. Эконом.и орг-ция пр-ва, лаб.4ч по п\гр, В-218'
        return
    
    if req['request']['original_utterance'].lower() in['эук-43']:
        res['response']['text'] = 'ПН\n8.30-11.40 2-7н. Практика производственная, лек., пр.з.4ч, Г-606\n12.20-15.30 2,7-10н. Всеобщее упр-ние качеством, лек., пр.з.4ч, В-309\nВТ\n8.30-11.40 1-10н. Практика производственная, лек., пр.з.4ч,  ст.пр.В.В.Кочерова\n12.20-15.30 1-10н. Всеобщее упр-ние качеством, лек., пр.з.4ч, В-306, ст.пр.Е.В.Шастина\nЧТ\n12.20-15.30 1-6, 8,10н. Стратег.управл.орг-цией, лек., пр.з.4ч, проф.А.А.Киселев, А-413\nПТ\n12.20-15.30 1-8н. Основы предпринимательства, лек., пр.з.4ч, А-408, ст.пр.Л.А.Танякина'
        return
    
    if req['request']['original_utterance'].lower() in['эис-44']:
        res['response']['text'] = 'ПН\n12.20-15.30 1-5н. Защита интеллектуальной собственности, лек.4ч, доц.В.Г.Копыльцов, Г-909\n15.40-19.00 2-5н. Защита интелл. собст-сти, пр.з.4ч, Г-909\nВТ\n8.30-11.40 2-6н. БЖД, лаб.4ч по п\гр, Г-721\n12.20-15.30 2-4н. БЖД, пр.з.4ч, Г-803\n15.40-19.00 1н. Защита интеллектуальной собственности, лек.4ч, доц.В.Г.Копыльцов, Г-909\nСР\n8.30-11.40 1-6н. БЖД, лек.4ч, проф.О.П.Филиппова, Г-904\nЧТ\n8.30-11.40 3н. БЖД, лаб.4ч по п\гр, Г-721\n5-6н. БЖД, пр.з.4ч, Г-903\n12.20-15.30 2н. Защита интелл. собст-сти, пр.з.4ч, В-306\nПТ\n12.20-15.30 1-6н. Интеллект.системы и технологии, лек.4ч, ст.пр.А.В.Герасимов, Г-506\n15.40-19.00 2-6н. Интел.инф.системы лаб.4ч по п\гр, Г-505\nСБ\n8.30-11.40 1-2н. Интеллектуальные системы и технологии, лек.4ч, 1н- Г-809, 2н - Г-506\n3-6н. Интел.системы и технологии, лаб.4ч по п\гр, Г-505\n12.20-15.30 2-6н. Интел.системы и технологии, пр.з.4ч, Г-801\n15.40-19.00 4-6н. Интел.системы и технологии, лаб.4ч по п\гр, Г-507'
        return
    
    if req['request']['original_utterance'].lower() in['эис-45']:
        res['response']['text'] = 'ПН\n12.20-15.30 1-5н. Защита интеллектуальной собственности, лек.4ч, доц.В.Г.Копыльцов, Г-909\nВТ\n8.30-11.40 2-6н. БЖД, пр.з.4ч, Г-803\n12.20-15.30 2-6н. БЖД, лаб.4ч по п\гр, Г-721\n15.40-19.00 1н. Защита интеллектуальной собственности, лек.4ч, доц.В.Г.Копыльцов, Г-909\nСР\n8.30-11.40 1-6н. БЖД, лек.4ч, проф.О.П.Филиппова, Г-904\n12.20-15.30 3-5н. БЖД, лаб.4ч по п\гр, Г-721\n2-6н. Интеллект.сис-темы и технологии, лаб.4ч по п\гр, Г-507 \nЧТ\n8.30-11.40 2-5н. Инт.системы и технологии, лаб.4ч по п\гр, Г-507\n12.20-15.30 3-6н. Защита интелл. собст-сти, пр.з.4ч, В-306\nПТ\n12.20-15.30 1-6н. Интеллект.системы и технологии, лек.4ч, ст.пр.А.В.Герасимов, Г-506\nСБ\n8.30-11.40 1-2н. Интеллектуальные системы и технологии, лек.4ч, 1н- Г-809, 2н - Г-506\n3-5н. Интел.системы и технологии, лаб.4ч по п\гр, Г-507\n12.20-15.30 2-6н. Интел.системы и технологии, пр.з.4ч, Г-808'
        return
    
    if req['request']['original_utterance'].lower() in['эпи-41']:
        res['response']['text'] = 'ПН\n12.20-15.30 2-5н. Экономика информац.систем, лек.4ч, Г-606, ст.пр.В.В.Кочерова\n15.40-19.00 2-5н. Эконом.информ. систем, лаб.4ч по п\гр, Г-501\nВТ\n12.20-15.30 1, 3-5н. Защита интеллектуальной собственности, лек., пр.з.4ч, Г-608, доц.Ю.В.Горовой\n15.40-19.00 2-5н. Эконом.информ. систем, лаб.4ч по п\гр, Г-501\nСР\n8.30-11.40 1-5н. Защита интеллектуальной собственности, лек., пр.з.4ч, Г-608\nЧТ\n12.20-15.30 1н. Эконом.информац. систем, лек.4ч, Г-606\n2-5н. Эконом.инф. систем, лаб.4ч по п\гр, Г-501\n15.40-19.00 1,3,5н Защита интелл. собст-сти, пр.з.4ч, Г-608\nПТ\n15.40-19.00 1,2,4н. Эконом.инф. систем, лаб.4ч по п\гр, Г-501\n3н. Экономика информ. систем, лек.4ч, Г-613'
        return
    
    if req['request']['original_utterance'].lower() in['эи-48']:
        res['response']['text'] = 'ПН\n12.20-15.30 1-8н. Упр-ние интеллект.собств-стью, лек., пр.з.4ч, доц.А.В.Кольцова, В-202\n15.40-19.00 1-7н. Интеллект. информац.системы, лек.4ч, Г-606 доц.А.В.Никитенко\nВТ\n15.40-19.00 1-2н. БЖД, лек.4ч, доц.В.В.Макарьин, Г-908\nСР\n8.30-11.40 1н. Информац. безопасность и защита инф-ции, лек.4ч, Г-606\n6-12н. Интелл.инф. системы, лаб.4ч, Г-507\n12.20-15.30 2-5н. Информац. безопасность и защита инф-ции, лек.4ч, Г-613 доц.А.В.Никитенко\n7-12н.  Инф.безоп.и ЗИ, лаб.4ч, Г-507\n15.40-19.00 3-5н. Инф.безоп.и ЗИ, лаб.4ч, Г-507\nЧТ\n8.30-11.40 Н\н с 1 по 11н. Управление интеллект.собст-стью, лек., пр.з.4ч, доц.А.В.Кольцова, В-217\nПТ\n12.20-15.30 7-12н. БЖД, пр.з.4ч, Г-903\n15.40-19.00 1-4н. БЖД, лек.4ч, Г-908\n9-10н. Интеллек.инф.системы, лаб.4ч, Г-505'
        return

    res['response']['text'] = 'К сожалению, я не понимаю тебя. Попробуй ещё раз ввести название своей группы, например, "ЭСМ-42" или введи "помощь" для того, чтобы запросить информацию о возможностях навыка.'
    
