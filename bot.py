from telebot import types
import telebot

bot = telebot.TeleBot('5064022412:AAHqmar1new04Lxd1BAVamwwH9pb7EXOmls')

name = ''


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == "Привет":
        keyboard = types.InlineKeyboardMarkup()
        key_reg = types.InlineKeyboardButton(text='✌', callback_data='reg')
        keyboard.add(key_reg)
        bot.send_message(message.from_user.id, 'Нажми кнопку для регистрации', reply_markup=keyboard)
        for pv_id in range((message.message_id - 50), message.message_id):
            bot.delete_message(message.chat.id, pv_id)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, 'Напиши "Привет"')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def get_name(message):
    global name
    name = message.text
    hello = 'Привет, ' + name + '! Введите /run'
    bot.send_message(message.from_user.id, text=hello)
    bot.register_next_step_handler(message, choices)


@bot.message_handler(commands=['run'], content_types=['text'])
def choices(message):
    keyboard = types.InlineKeyboardMarkup()
    key_c1 = types.InlineKeyboardButton(text='1. Посмотреть информацию о маршрутах', callback_data='c1')
    keyboard.add(key_c1)
    key_c2 = types.InlineKeyboardButton(text='2. Описание бота', callback_data='c2')
    keyboard.add(key_c2)
    key_c3 = types.InlineKeyboardButton(text='3. Информация о создателях', callback_data='c3')
    keyboard.add(key_c3)
    bot.send_message(message.from_user.id, """Вы вошли в Omsk Travel Guide

Выберите действие:""", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    keyboard = types.InlineKeyboardMarkup()
    if call.data == "reg":
        bot.send_message(call.message.chat.id, "Как тебя зовут?")
        bot.register_next_step_handler(call.message, get_name)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == "c1":
        key_wc1 = types.InlineKeyboardButton(text='1. История', callback_data='wc1')
        keyboard.add(key_wc1)

        key_wc2 = types.InlineKeyboardButton(text='2. Красивые места', callback_data='wc2')
        keyboard.add(key_wc2)

        key_wc3 = types.InlineKeyboardButton(text='3. Достоевский', callback_data='wc3')
        keyboard.add(key_wc3)

        key_back = types.InlineKeyboardButton(text='Вернуться к меню', callback_data='back')
        keyboard.add(key_back)

        bot.send_message(call.message.chat.id, "Выберите маршрут:", reply_markup=keyboard)

    elif call.data == "wc1":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='1')
        keyboard.add(key_n)
        key_return = types.InlineKeyboardButton(text='Вернуться к выбору', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, 'Вы выбрали маршрут "История"', reply_markup=keyboard)

    elif call.data == "1":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='2')
        keyboard.add(key_n)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """1. Омская крепость
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "2":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='3')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='1')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """2. Тарские ворота
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "3":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='4')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='2')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """3. Успенский собор
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "4":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='5')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='3')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """4. Омский гос академ театр
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "5":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='6')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='4')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """5. Памятник слесарю
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "6":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='7')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='5')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """6. Памятник городовому
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "7":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='8')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='6')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """7. Омский краеведческий музей
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "8":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='9')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='7')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """8. ТЮЗ
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "9":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='10')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='8')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """9. Омский кадетский корпус (4 памятника)- старый
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "10":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='11')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='9')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """10. Дом Хлебникова
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "11":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='12')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='10')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """11. Парк Победы
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "12":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='13')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='11')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """12. Лютеранская церковь Урала
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "13":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='14')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='12')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """13. Казачий собор
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "14":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='15')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='13')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """14. Мемориал «Вечный огонь»
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "15":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='16')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='14')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """15. Площадь Бухгольца
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "16":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='17')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='15')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """16. Памятник «труженикам тыла»
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "17":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='18')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='16')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """17. Скульптура «Люба»
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "18":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='19')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='17')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """18. Дом со шпилем
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "19":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='20')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='18')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """19. Каланча
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "20":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='21')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='19')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """20. Здание гауптвахты
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "21":
        key_end = types.InlineKeyboardButton(text='Закончить', callback_data='end')
        keyboard.add(key_end)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='20')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='wc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """21. ЖД вокзал
Описание""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "c2":
        key_back = types.InlineKeyboardButton(text='Вернуться к выбору', callback_data='back')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Omsk Travel Guide – бот-путеводитель для жителей и гостей города Омска. Программа позволяет выбрать наиболее известные и понравившиеся достопримечательности, предложенные разработчиками, основываясь на местоположении пользователя. Бот дает возможность увидеть изображение, адрес и краткую аннотацию выбранных объектов.", reply_markup=keyboard)

    elif call.data == "c3":
        key_back = types.InlineKeyboardButton(text='Вернуться к выбору', callback_data='back')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Группа БИТ-211. Лидер группы: Краля Алексей - участие в принятии креативных решений, разработка блоков приложения, создание календарного плана работ; Тестировщик: Сучкова Алина - участие в принятии креативных решений, разработка плана тестирования, тестирование приложения, выявление багов; Аналитик: Нагний Екатерина - создание и проработка технического задания, участие в принятии креативных решений; Разработчики: Сизов Данила - главный разработчик; Устименко Любовь - участие в принятии креативных решений, разработка программы; Поречин Роман - разработка программы; Крючков Андрей - разработка программы.", reply_markup=keyboard)

    elif call.data == "back":
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == "end":
        bot.send_message(call.message.chat.id, 'Досвидания! Спасибо за использование Omsk Travel Guide')

    elif call.data == "rc1":
        key_wc1 = types.InlineKeyboardButton(text='1. История', callback_data='wc1')
        keyboard.add(key_wc1)

        key_wc2 = types.InlineKeyboardButton(text='2. Красивые места', callback_data='wc2')
        keyboard.add(key_wc2)

        key_wc3 = types.InlineKeyboardButton(text='3. Достоевский', callback_data='wc3')
        keyboard.add(key_wc3)

        key_back = types.InlineKeyboardButton(text='Вернуться к меню', callback_data='back')
        keyboard.add(key_back)

        bot.send_message(call.message.chat.id, "Выберите маршрут:", reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)


bot.infinity_polling()