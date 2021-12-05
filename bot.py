#!/usr/local/bin/python
# -*- coding: utf-8 -*-
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
        for pv_id in range((message.message_id-50), message.message_id):
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
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """1. Омская крепость
Адрес: Партизанская ул., 5А

Омская крепость – историко-культурный туристический комплекс, состоящий из реконструированных и восстановленных фрагментов форпоста, с которого началась славная история Омска. Самая первая крепость была построена в начале 18 столетия, вторая, гораздо большей площади – спустя полвека. Одной из ярких достопримечательностей исторического комплекса является дом, в котором некогда жил комендант крепости. На территории комплекса работает музей воинской славы, под открытым небом выставлена боевая техника. Здесь можно посетить тематическую выставку или в кинозале посмотреть документальный фильм о городе.""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "2":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='3')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='1')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """2. Тарские ворота
Адрес: Спартаковская ул.

Тарские ворота – один из символов города. Они известны тем, что через них проходил ссыльный Федор Достоевский, который отбывал каторгу в Омском остроге. 
Ворота были построены в 1792 году в качестве входа в Степной бастион крепости, в которой располагался каторжный острог. В 1959 году ворота были уничтожены из-за того, что они не вписывались в окружающий ландшафт, но позже ворота отстроили на новом месте. Новые ворота были построены в 1991 году с некоторыми отклонениями от своего оригинала. Внутри свода вместо двух ниш были сделаны четыре ниши. В одной из ниш была встроена дверь на лестницу, ведущую в караульную комнату площадью 30 квадратных метров.""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "3":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='4')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='2')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, ("3. Успенский собор\n"
                                                "Адрес: Тарская ул., 7\n"
                                                "\n"
                                                "Самый важный храм Омска, один из самых красивых и величественных в России, Свято-Успенский кафедральный собор признан уникальным памятником русского зодчества. Церковь была возведена на излете 19 века, в основе – проект знаменитого Санкт-Петербургского Храма Спаса-на-Крови. После октябрьской революции Свято-Успенский кафедральный собор разделил участь большинства культовых сооружений. При восстановлении церкви в 2000-е годы были обнаружены иконы и мощи архиепископа Сильвестра Сибирского, расстрелянного большевиками и канонизированного епархией как новомученик. Сейчас старинные иконы и рака с мощами святого хранятся в здании собора."))
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "4":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='5')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='3')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, ("4. Омский гос академ театр\n"
                                                "Адрес: ул. Ленина, 8А\n"
                                                "\n"
                                                "Омский академический театр драмы – старейший драмтеатр в Сибири, принявший первых зрителей в 1875 году. Оно получилось эклектичным, классическая основа декорирована сложными, замысловатыми элементами в стиле барокко. В нишах установлены бюсты великих русских писателей, а фронтон украшает оригинальная скульптура работы чешского мастера Винклера «Крылатый гений» – фигурка ангела, словно парящая в воздухе. Основа репертуара театра – спектакли по классическим произведениям, но есть и современные, экспериментальные постановки. Театр не единожды получал престижные награды."))
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "5":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='6')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='4')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """5. Памятник слесарю
Адрес: ул. Карла Либкнехта, 5

Омский памятник слесарю-сантехнику «Степаныч» появился в городе в 1998 году. С момента установки он стал и остается по сей день одной из самых фотографируемых городских скульптур. Памятник сантехнику в Омске является олицетворением уважения горожан к профессии. Памятник представляет собой сантехника, который выглядывает из канализационного люка, на котором лежит разводной ключ. Сантехник в защитной каске положил под подбородок руки и наблюдает городскую суету. Добродушная улыбка Степаныча, его задумчивый взгляд непременно вызывают ответную улыбку. Памятник заслуженно называют самым обаятельным и душевным.""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "6":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='7')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='5')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """6. Памятник городовому
Адрес: улица Щербанёва, 2

В ноябре 2011 года компания скульптурных композиций, изображающих исторических персонажей, пополнилась новой скульптурой - городовым. Отлитый из бронзы страж порядка высотой 180 сантиметров охраняет перекресток улиц Ленина и Партизанской, напротив Серафимо-Алексеевской часовни, в непосредственной близости от ресторана "Гермелин". Страж порядка выглядит очень реалистично: он экипирован револьвером, шашкой и свистком. Он щегольски подкручивает ус и наблюдает за жизнью на оживленных улицах Омска.""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "7":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='8')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='6')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """7. Омский краеведческий музей
Адрес: ул. Ленина, 23 А

Один из первых музеев России. Музей был открыт в 1878 году по инициативе русских учёных, первые выставки состояли из частных пожертвований. В годы Великой Отечественной войны в здании хранились ценные коллекции, вывезенные из музеев городов, оккупированных немцами. За время своего существования музей Омска собрал выдающееся количество экспонатов - более двухсот тысяч. Постоянные выставки, распологаются в 6 залах, рассказывают об истории региона от каменного века до современности, о разнообразной, удивительной природе Омской области. Экспозиции состоят из археологических находок, макетов старинных зданий, чучел, птиц и животных, военных и бытовых орудий, предметов искусства, икон, монет, документов.""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "8":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='9')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='7')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """8. ТЮЗ
Адрес: просп. Карла Маркса, 4В

ТЮЗ в Омске основан в 1937 году по инициативе омских пионеров. Высокий уровень театральных постановок был задан режиссером Николаем Павловичем Охлопковым, который руководил учреждением, будучи в эвакуации в годы Великой Отечественной войны. С 1967 года ТЮЗ располагается в построенном для него здании на проспекте Карла Маркса напротив Театрального сквера. За прошедшие годы коллективы детского театра в Омске подготовили и показали зрителям более 500 спектаклей. Помимо спектаклей, в омском ТЮЗе проходит множество разноплановых мероприятий: вечера классической музыки и литературы, творческие встречи с коллективом театра, мастер-классы и лекции для школьников, обсуждение театральных постановок, экскурсии по театральному закулисью.""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "9":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='10')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='8')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """9. Омский кадетский корпус (4 памятника)- старый
Адрес: ул. Ленина, 26

Здание Сибирского кадетского корпуса является одним из наиболее величественных монументальных зданий Омска первой половины XIX века. Обрастая пристройками, это самое крупное учебное заведение города оставалось таким на протяжении более 100 лет. В мае 1813 года в Омске было открыто первое военно-учебное заведение Сибири – Войсковое казачье училище. Двухэтажное, на высоком цоколе с шестиколонным ионическим портиком, являющимся главным акцентом строения, здание привлекает внимание соразмерностью своих деталей и стилевой завершенностью. После бывшей гауптвахты и казармы в крепости – это одно из самых старых двухэтажных кирпичных зданий, сохранившихся до наших дней.""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "10":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='11')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='9')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """10. Дом Хлебникова
Адрес: ул. Почтовая, д. 27 / ул. Сажинская, д. 45

Дом был построен по проекту Арсения Хлебникова — общественного деятеля, адвоката и музыканта, которого выселили в Сибирь в 1887 году. В здании не раз проходили литературно-музыкальные вечера, которые посещали выдающиеся люди города: музыкант Виссарион Шебалин, ученый Пётр Драверт, поэт Леонид Мартынов. В доме общей площадью 250 квадратных метров были два кабинета, столовая, гостиная, две детских и одна спальня родителей, кухня и веранда, которая выходила в сад. К северному фасаду здания со стороны кухни были пристроены сени. Кроме того, дом был оформлен резными гирляндами растительного орнамента с элементами модерна.""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "11":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='12')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='10')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, ("11. Парк Победы\n"
                                                "Адрес: ул. Андрианова, 3\n"
                                                "\n"
                                                "Самая масштабная по площади (более 70 га) благоустроенная зеленая зона Омска – парк культуры и отдыха имени 30-летия ВЛКСМ. Парк был заложен в 1940 году на месте лесного массива как Центральный, а в юбилейный для советской молодежи год получил название, используемое и поныне. Парк – место знаковое, многие омичи в летний воскресный день 1941 года именно здесь услышали горькую и страшную новость о нападении Германии на СССР. Сегодня \"комсомольский\" парк целиком и полностью ориентирован на комфортный отдых и беззаботное времяпрепровождение. Среди густых зарослей парка и вокруг пруда проложены удобные аллеи, работает масса аттракционов."))
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "12":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='13')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='11')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, ("12. Лютеранская церковь Урала\n"
                                                "Адрес: ул. Рождественского, 2/1\n"
                                                "\n"
                                                "Лютеранская церковь Святой Екатерины – единственное здание культового назначения, сохранившееся с 18 века. Построенная на исходе столетия, каменная церковь была уже третьим по счету храмом лютеран в Омске и могла одновременно вместить более 100 человек. В свое время церковь посещали многие государственные чины. Храм принимал прихожан без малого полтора столетия, закрыли его в 1930 году. В 80-х годах прошлого века здание бывшей лютеранской церкви отремонтировали, убрали культовые элементы с фасада и из внутренних помещений. Сейчас здесь хранятся коллекции Музея областного УВД."))
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "13":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='14')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='12')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, ("13. Казачий собор\n"
                                                "Адрес: ул. Ленина, 27\n"
                                                "\n"
                                                "Никольский Казачий собор – самый «возрастной» храм Омска, его возвели в начале 19 века. Никольский собор – единственное культовое сооружение в Омске, неразрушенное во время правления Советов. Церковь выполнена в стиле позднего классицизма. Почти столетие церковь владела исторической реликвией – настоящим знаменем войска Ермака. Но в неразберихе гражданской войны стяг похитили, и сейчас выставлена его точная копия. В Казачьем соборе также хранятся святые мощи угодников, в том числе Георгия Победоносца, Серафима Саровского, Сергия Радонежского."))
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "14":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='15')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='13')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """14. Мемориал «Вечный огонь»
Адрес: Центральный округ, Мемориальный сквер Памяти борцов революции 

Мемориальный сквер (Вечный огонь) – одна из достопримечательностей Омска. Создан он был в честь памяти о жертвах Октябрьской революции. Представляет собой целый сквер, который был отдан для этой цели в 1966 году. Но власти не ограничились только лишь облагораживанием данного сквера. Здесь были перезахоронены останки павших, сражавшихся за свободу. Именно поэтому сквер стал мемориальным. 6 ноября 1967 года сквер переименовали в Сквер Борцов Революции. Здесь был установлен Вечный огонь.""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "15":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='16')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='14')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """15. Площадь Бухгольца

В месте слияний Оми и Иртыша располагается центральная площадь города. Место историческое, как полагают, именно здесь в 1716 году была заложена крепость – предтеча современного Омска. Площадь носит имя генерала Ивана Бухгольца, по указу Петра I возглавлявшего военную экспедицию, и как раз основавш уютное пространство вдали от шумных магистралей, с ухоженными газонами и мощенными аллеями. Центр площади украшает гигантский (7 м в диаметре) металлический шар «Держава». На его поверхности располагаются панно, иллюстрирующие различные моменты исследования и покорения Сибирской земли.""")
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "16":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='17')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='15')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, ("16. Памятник «труженикам тыла»\n"
                                                "Адрес: Октябрьский округ\n"
                                                "\n"
                                                "Памятник труженикам тыла в г. Омске символизирует вечную память омичам, которые в годы Великой Отечественной войны каждый по-своему трудился ради победы. В 2010-м году седьмого мая в торжественной обстановке состоялось открытие этого памятника в честь 65-летия празднования Дня Победы. В центре памятника располагается двусторонняя группа скульптур, которая является прообразом тыловиков Омска в военное время. В эту композицию входят: женщина-мать с младенцем на руках, крестьянка, которая собирается на покос, рабочий оборонного завода, мальчик пастух, девочка, медработник и др. Связующее звено между «деревней» и «городом» - длинный военный эшелон, направляющийся на фронт. Огромные белые крылья в основе памятника."))
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "17":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='18')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='16')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, ("17. Скульптура «Люба»\n"
                                                "Адрес: ул. Ленина, 7\n"
                                                "\n"
                                                "Скульптура «Люба» в городе Омске является одним из любимых достопримечательностей омичей. Это увековеченное изображение молодой девушки – Любови Гасфорд, которая была супругой Густава Гасфорда – одного из генерал-губернаторов Сибири в 19-м веке. Скульптор запечатлел тот момент, когда Люба (или как в народе еще называют скульптуру Любаша) вышла на прогулку и присела на скамейку. Горожане трепетно и с нежностью относятся к этой скульптуре, поскольку она олицетворяет собой женскую красоту и одновременно скромность, а также показывает частичку прошлого города Омска."))
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "18":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='19')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='17')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, ("18. Дом со шпилем\n"
                                                "Адрес: просп. Карла Маркса, 29\n"
                                                "\n"
                                                "В середине прошлого века многоэтажка была своего рода парадными воротами Омска. Венчала перекресток Маркса и Масленникова, которая в те годы называлась Перевозной. По задумке автора на этом месте должен был возвышаться целый архитектурный ансамбль — у Дома со шпилем мог появиться близнец."))
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "19":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='20')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='18')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, ("19. Каланча\n"
                                                "Адрес: Интернациональная ул., 41, корп. 2\n"
                                                "\n"
                                                "Пожарная каланча – колоритная достопримечательность Омска, своеобразный символ города. Конструкция из красного кирпича была построена в начале прошлого века, причем на том же месте, где ранее располагалась деревянная вышка. Назначение каланчи – следить с высоты за ситуацией в городе и оперативно реагировать на пожары, что особо актуально при массовой деревянной застройке. Каланча использовалась по прямому назначению до середины прошлого столетия. Сейчас это исторический и архитектурный памятник, внутри которого располагается музей. Экспозиции посвящены пожарной охране и рассказывают историю башни."))
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "20":
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='21')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='19')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, ("20. Здание гауптвахты\n"
                                                "Адрес: Партизанская ул., 14\n"
                                                "\n"
                                                "По ходу строительства новой омской крепости в ней стали появляться не только военные здания, но и гражданские. И наверное одним из первых подобных строений стало здание Гауптвахты, построенное в 1781 году. В свое время она являлось одним из самых красивых и больших каменных зданий в городе. В оригинальном виде здания присутствовала колоннада из шести колонн, соединяющая боковые выступы. Которая в последствии была разобрана. В помещениях гауптвахты изначально располагался караул крепости. Сейчас в этом здании располагается областной военкомат."))
        pic = 'https://i.pinimg.com/564x/57/8c/72/578c72fc2f2161e14605939e81fe97dc.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "21":
        key_end = types.InlineKeyboardButton(text='Закончить', callback_data='end')
        keyboard.add(key_end)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='20')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, ("21. ЖД вокзал\n"
                                                "Адрес: ул. Леконта, 1\n"
                                                "\n"
                                                "Омский ЖД вокзал был построен к 1896 году, в то же время, когда велось строительство Транссибирской магистрали. Это было одноэтажное здание с одним корпусом, таким сооружение просуществовало до 1914 года. С началом первой мировой войны пассажиропоток увеличился, активизировалась военная промышленность, и нагрузка на транспортную систему возросла. К 1958 реконструкция была завершена, и у вокзала появилось 3 этажа, изменился и внешний вид вокзала, возросло число направлений электропоездов. В 2004 году рядом с главным зданием построили второй корпус – пригородный вокзал."))
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
        bot.send_message(call.message.chat.id, 'До свидания! Спасибо за использование Omsk Travel Guide')
        bot.delete_message(call.message.chat.id, call.message.message_id)

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