import telebot
from telebot import types
import requests


token = '835349082:AAEcKcSmHNyFLlhnyE5-3msKit313Nk-sP0'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(
        message.chat.id, 
        'Здравствуйте! Я виртуальная помощница клиники. Я расскажу вам о всем, что только может вас заинтересовать.' + 
        '\nНу что, Начнем?', 
        reply_markup=keyboard1()
    )

def keyboard1():
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=True, 
        resize_keyboard=True
    )
    button_1 = types.KeyboardButton('Начать')
    markup.add(button_1)
    return markup
 
 
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Начать':
        bot.send_message(
            message.chat.id, 
            'Выберите направление, которое Вам более интересно, у Вас будет возможность вернуться в это меню еще раз: ', 
            reply_markup=keyboard2()
        )
    elif message.text == 'Подготовка к операции':
        bot.send_message(
            message.chat.id, 
            'Какой вид анестезии планируется?', 
            reply_markup=keyboard3()
        )
    elif message.text == 'Местная':
        bot.send_message(
            message.chat.id, 
            'Общие требования: \n1.Для предупреждения кровопотери и отечности тканей, операция назначается не в дни цикла \n2.Коррекция цифр артериального давления менее 140/70 мм.рт.ст \nЗ.Минимум за 3 недели до операции сократить табакокурение, в том числе и электронных сигарет. \n\n!!!АНАПИЗЫ !!! \n1)Общий анализ крови с определением количества тромбоцитов (дейст. 10 дней) \n2)Коагулограмма : АЧТВ , МНО , протромбин (дейст.10 дней) \n3)Биохимический анализ крови: глюкоза, общий билирубин, общий белок, креатинин, АЛТ, АСТ, электролиты,Na+, К+ , Cl- (10 дней) \n4)Анализ крови на групповую принадлежность и резус - фактор \n5)Общий анализ мочи (10 дней) \n6)Серология: ВИЧ, Гепатиты В и С, РW (действует 1 месяц) \n7)Экг (действует месяц)'
        )
        bot.send_message(message.chat.id, 'У вас остались какие-то вопросы?', reply_markup=keyboard4())
    elif message.text == 'Общая':
        bot.send_message(
            message.chat.id, 
            'Общие требования: \n1.Для предупреждения кровопотери и отечности тканей , операция назначается не в дни цикла! \n2.Коррекция цифр артериального давления менее 140/70 мм.рт.ст \n3.Минимум за 3 недели до операции сократить табакокурение, в том числе и электронных сигарет \n4.Для профилактики тромбоэмболии, отмена гормональных пероральных препаратов за 2 месяца до операции \n5.Перед операцией уменьшить длину ногтя для установки датчика пульсоксиметра \n6.Запрещается прием пищи в день операции за 8 часов до операции \n7.Вечером в день перед операцией. Очистительная клизма Микролакс \n8.В день операции: бритье области лона \n\n!!АНАЛИЗЫ!! \n1)Общий анализ крови с определением количества тромбоцитов (дейст. 10 дней) \n2)Коагулограмма: АЧТВ , МНО . протромбин (дейст. 10 дней) \n3)Биохимический анализ крови: Глюкоза, общий билирубин, общий белок, креатинин, АЛТ, АСТ, электролиты, Nа+, К+, CL(10 дней). \n4)Анализ крови на групповую принадлежность и резус - фактор \n5)Общий анализ мочи (10 дней) \n6)Серология: ВИЧ, Гепатиты В и С, РW (действует 1 месяц) \n7)Рентген грудной клетки (действует 1 год ) \n8)Зкг эхокардиограмма (действует 1 месяц) \n9)УЗИ вен нижних конечностей \n10)Узи передней брюшной стенки (либо узи молочных желез при маммопластике) \n11)Консультация терапевта (терапевт даёт выписку, что нет противопоказаний к хирургическому вмешательству)'
        )
        bot.send_message(
            message.chat.id, 
            'У вас остались какие-то вопросы?', 
            reply_markup=keyboard4()
        )
    elif message.text == 'Что необходимо взять с собой в клинику':
        bot.send_message(
            message.chat.id, 
            '📖 Паспорт \n🧾 ОРИГИНАЛЫ АНАЛИЗОВ  \n💰 ОПЛАТУ ( возможна оплата картой ) \nКОМПРЕССИОННЫЕ ЧУЛКИ 1 ЛИБО 2 КЛАСС КОМПРЕССИИ (берете с собой в клинику) \n\nНУ И САААМОЕ ВАЖНОЕ  \n😁 ХОРОШЕЕ НАСТРОЕНИЕ'
        )
    elif message.text == 'Как попасть к Вам, если я из Москвы и МО':
        bot.send_message(
            message.chat.id, 
            '1.присылайте фото или видео @darinarubinina \n2.указываете дату цикла, после чего согласовываем дату операции \n3.вносите предоплату 10 %  по выставленному счёту \n4.за 10 дней до операции сдаёте анализы 💉 и высылаете их по готовности на этот номер телефона \n❗(Если по результатам анализов операция невозможна, то предоплата возвращается в полном объёме )❗ \n5. Приезжаете 🚗 в назначенный день подготовленные (ни куска еды, ни глотка воды, жвачку не жуем...если рот и горло сохнут - можно прополоскать и все выплюнуть),  не забывайте про  компрессионные чулки, а также хорошее настроение 🤩 \n\nЕсли есть возможность приехать на консультацию, то напишите желаемую дату консультации @darinarubinina', 
            reply_markup=keyboard7()
        )
    elif message.text == 'Как попасть к Вам, если я из другого города':
        bot.send_message(
            message.chat.id, 
            '1.присылайте фото или видео @darinarubinina \n2.указываете дату цикла, после чего согласовываем дату операции \n3.вносите предоплату 10 %  по выставленному счёту \n4.за 10 дней до операции сдаёте анализы 💉 и высылаете их по готовности на этот номер телефона  \n❗(Если по результатам анализов операция невозможна , то предоплата возвращается в полном объёме )❗ \n5. Приезжаете 🚗 в назначенный день подготовленные (ни куска еды, ни глотка воды, жвачку не жуем...если рот и горло сохнут - можно прополоскать и все выплюнуть),  не забывайте про  компрессионные чулки, а также хорошее настроение 🤩  \n\nЕсли необходима помощь в бронировании гостиницы, напишите об этом @darinarubinina \n\nЕсли необходима встреча, укажите дату прилета, аэропорт ,номер рейса и время @darinarubinina', 
            reply_markup=keyboard7()
        )
    elif message.text == 'Уточнить стоимость операции':
        bot.send_message(
            message.chat.id, 
            'Выберите:', 
            reply_markup=keyboard5()
        )
    elif message.text == 'Лицо':
        bot.send_message(
            message.chat.id, 
            'Височный лифтинг от 150 000 Р Эндоскопическая подтяжка лба от 150 000 Р \n\nПодтяжка средней зоны лица от 150 000 Р \n\nПодтяжка шеи от 150 000 Р Подтяжка 2/3 лица и шеи от 2В0 000 Р \n\nБлефаропластика верхних век под местной анестезией 50 000 Р \n\nБлефаропластика верхних век под общей анестезией 60 000 Р \n\nБлефаропластика верхних век с пексией бровей (фиксацией бровей) под местной анестезией 80 000 Р \n\nБлефаропластика верхних век с пексией бровей (фиксацией бровей) под общей анестезией 90 000 Р \n\nБлефаропластика нижних век под местной анестезией 80 000 Р \n\nБлефаропластика нижних век под общей анестезией 90 000 Р \n\nБлефаропластика нижних век с миопексией под местной анестезией 110 000 Р \n\nБлефаропластика нижних век с миопексией под общей анестезией 120 000 Р Изменение разреза глаза 100 000 Р \n\nРинопластика от 280 000 рублей'
        )
        bot.send_message(
            message.chat.id, 
            'У вас остались какие-то вопросы?', 
            reply_markup=keyboard4()
        )
    elif message.text == 'Тело':
        bot.send_message(
            message.chat.id, 
            'Мини абдоминопластика от 230000 Р \n\nАбдоминопластика с ушиванием диастаза и транслркацией пупочного ложа от 285000 Р \n\nУвеличение груди (стоимость имплантов включена) от 265000 Р \n\nУвеличение груди с подтяжкой (стоимость имплантов включена) от 285 000 Р \n\nРедукционная (уменьшение) маммопластика от 290 000 Р \n\nПодтяжка груди без имплантов от 240 000 Р \n\nЛипофилинг ягодиц от 360 ООО Р \n\nЛипомоделирование живот от 180 000 Р \n\nЛипомоделирование живот /Бока /спина от 240 000 Р \n\nЛипомоделирование ног.от 180 000 Р \n\nЛипомоделирование рук от 60 000 Р \n\nБрахиопластика от 200 000 Р'
        )
        bot.send_message(
            message.chat.id, 
            'У вас остались какие-то вопросы?', 
            reply_markup=keyboard4()
        )
    elif message.text == 'Хочу узнать, как записаться на рекламную операцию':
        bot.send_message(
            message.chat.id, 
            'Выберите:', 
            reply_markup=keyboard6()
        )
    elif message.text == 'Абдоминопластика':
        bot.send_message(
            message.chat.id, 
            'Стоимость рекламной абдоминопластики составляет 180 000 р. \nОтдельно оплачивается компрессионное белье 4500 р. месяц с момента операции \nВы ведете дневник в INSTAGRAM , где описываете свою реабилитацию, свои ощущения и тд. в день должно быть мин 1 фото!!! \nАнализы Вы сдаете самостоятельно После данной операции Вы проводите в стационаре 48 часов, последующее пребывание оплачивается отдельно (6000 р/сутки) Снятие швов с пупка на 14 день после операции. Если Вы из другого города планируйте оставаться в Москве 5 дней после операции'
        )
        bot.send_message(
            message.chat.id, 
            'У вас остались какие-то вопросы?', 
            reply_markup=keyboard4()
        )
    elif message.text == 'Липомодерирование живот, бока, спина':
        bot.send_message(
            message.chat.id, 
            'Стоимость рекламной операции по липомоделированию 360" составляет 180 000 р. \nОтдельно оплачивается компрессионное белье 6500 р. Месяц с момента операции \nВы ведете дневник в INSTAGRAM , где описываете свою реабилитацию, свои ощущения и тд. в день должно быть мин 1 фото!!! \nАнализы Вы сдаете самостоятельно После данной операции Вы проводите в стационаре 48 часов, последующее пребывание оплачивается отдельно (6000 р/сугки) Снятие швов с пупка на 14 день после операции. Если Вы из другого города планируйте оставаться в Москве 5 дней после операции. У Вас остались вопросы?'
        )
        bot.send_message(
            message.chat.id, 
            'У вас остались какие-то вопросы?', 
            reply_markup=keyboard4()
        )
    elif message.text == 'Увеличивание груди':
        bot.send_message(
            message.chat.id, 
            'Стоимость рекламной операции по увеличению груди составляет 150 000 р. \nОтдельно оплачивается компрессионное белье 5450 р. Месяц с момента операции \nВы ведете дневник в INSTAGRAM , где описываете свою реабилитацию, свои ощущения и тд. в день должно быть мин 1 фото!!! Анализы Вы сдаете самостоятельно. Мы используем круглые импланты фирмы МЕNТОР? с пожизненной гарантией (стоимость имплантов входит в стоимость) После данной операции Вы проводите в стационаре 24 часа, последующее пребывание оплачивается отдельно (6000 р/сутки) Первый осмотр состоится на 5 день после операции. Если Вы из другого города планируйте оставаться в Москве 5 дней после операции'
        )
        bot.send_message(
            message.chat.id, 
            'У вас остались какие-то вопросы?', 
            reply_markup=keyboard4()
        )
    elif message.text == 'Восстановление после родов':
        bot.send_message(
            message.chat.id, 
            'Стоимость рекламной абдоминопластики составляет 180 000 р, стоимость рекламной операции по подтяжке груди с увеличением 240 000 р. \nОтдельно оплачивается компрессионное белье 4500 р и бандаж на грудь 5450 р. Месяц с момента операции \nВы ведете дневник в INSTAGRAM, где описываете свою реабилитацию, свои ощущения и тд. в день должно быть мин 1 фото!!! Анализы Вы сдаете самостоятельно После данной операции Вы проводите в стационаре 48 часов, последующее пребывание оплачивается отдельно (6000 р/сутки) Снятие швов с груди на 5 день, а с пупка на 14 день после операции. Если Вы из другого города планируйте оставаться в Москве 5 дней после операции'
        )
        bot.send_message(
            message.chat.id, 
            'У вас остались какие-то вопросы?', 
            reply_markup=keyboard4()
        )
    elif message.text == 'Липофилинг':
        bot.send_message(
            message.chat.id, 
            'Стоимость рекламной операции по липофилингу ягодиц составляет 250 000 р.! \nОтдельно оплачивается компрессионное белье 10450 р Месяц с момента операции \nВы ведете дневник в INSTAGRAM , где описываете свою реабилитацию, свои ощущения и тд. в день должно быть мин 1 фото!!! Анализы Вы сдаете самостоятельно После данной операции Вы проводите в стационаре 48 часов, последующее пребывание оплачивается отдельно (6000 р/сугки) Снятие швов на 5 день. Если Вы из другого города планируйте оставаться в Москве 5 дней после операции'
        )
        bot.send_message(
            message.chat.id, 
            'У вас остались какие-то вопросы?', 
            reply_markup=keyboard4()
        )
    elif message.text == 'Хочу записаться на операцию, консультацию':
        bot.send_message(
            message.chat.id, 
            'Пишите @darinarubinina'
        )
    elif message.text == 'Назад':
        bot.send_message(
            message.chat.id, 
            'Выберите направление, которое Вам более интересно, у Вас будет возможность вернуться в это меню еще раз: ', 
            reply_markup=keyboard2()
        )
    elif message.text == 'Да':
        bot.send_message(
            message.chat.id, 
            'свяжитесь с @darinarubinina'
        )
    elif message.text == 'Нет':
        bot.send_message(
            message.chat.id, 
            'Будем рады видеть Вас в клинике Newme 💜'
        )


def keyboard2():
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=True, 
        resize_keyboard=True
    )
    button_1 = types.KeyboardButton('Подготовка к операции')
    button_2 = types.KeyboardButton('Что необходимо взять с собой в клинику')
    button_3 = types.KeyboardButton('Как попасть к Вам, если я из Москвы и МО')
    button_4 = types.KeyboardButton('Как попасть к Вам, если я из другого города')
    button_5 = types.KeyboardButton('Уточнить стоимость операции')
    button_6 = types.KeyboardButton('Хочу узнать, как записаться на рекламную операцию')
    button_7 = types.KeyboardButton('Хочу записаться на операцию, консультацию')
    markup.add(button_1)
    markup.add(button_2)
    markup.add(button_3)
    markup.add(button_4)
    markup.add(button_5)
    markup.add(button_6)
    markup.add(button_7)
    return markup

def keyboard3():
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=True, 
        resize_keyboard=True
    )
    button_1 = types.KeyboardButton('Местная')
    button_2 = types.KeyboardButton('Общая')
    markup.add(button_1)
    markup.add(button_2)
    return markup

def keyboard4():
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=True, 
        resize_keyboard=True
    )
    button_1 = types.KeyboardButton('Да')
    button_2 = types.KeyboardButton('Нет')
    button_3 = types.KeyboardButton('Назад')
    markup.add(button_1)
    markup.add(button_2)
    markup.add(button_3)
    return markup

def keyboard5():
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=True, 
        resize_keyboard=True
    )
    button_1 = types.KeyboardButton('Лицо')
    button_2 = types.KeyboardButton('Тело')
    markup.add(button_1)
    markup.add(button_2)
    return markup

def keyboard6():
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=True, 
        resize_keyboard=True
    )
    button_1 = types.KeyboardButton('Абдоминопластика')
    button_2 = types.KeyboardButton('Липомодерирование живот, бока, спина')
    button_3 = types.KeyboardButton('Увеличивание груди')
    button_4 = types.KeyboardButton('Восстановление после родов')
    button_5 = types.KeyboardButton('Липофилинг')
    markup.add(button_1)
    markup.add(button_2)
    markup.add(button_3)
    markup.add(button_4)
    markup.add(button_5)
    return markup

def keyboard7():
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=True, 
        resize_keyboard=True
    )
    button_1 = types.KeyboardButton('Назад')
    markup.add(button_1)
    return markup

bot.polling(
    none_stop=True, 
    interval=0
)
