#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from telebot import types
import telebot

bot = telebot.TeleBot('5064022412:AAHqmar1new04Lxd1BAVamwwH9pb7EXOmls')


@bot.message_handler(commands=['start'], content_types=['text'])  # основное меню бота
def choices(message):
    keyboard = types.InlineKeyboardMarkup()  # добавление клавиатуры для кнопок
    key_c1 = types.InlineKeyboardButton(text='1. Посмотреть информацию о маршрутах', callback_data='c1')
    keyboard.add(key_c1)
    key_c2 = types.InlineKeyboardButton(text='2. Описание бота', callback_data='c2')
    keyboard.add(key_c2)
    key_c3 = types.InlineKeyboardButton(text='3. Информация о создателях', callback_data='c3')
    keyboard.add(key_c3)
    bot.send_message(message.from_user.id, """Приветствуем вас, пользователь.
Omsk Travel Guide – ваш первональный гид по Омску!

Вы можете выбрать одно из предложенных действий:""", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)  # функции бота
def callback(call):
    keyboard = types.InlineKeyboardMarkup()  # добавление клавиатуры для кнопок

    if call.data == "c1":  # отзыв на нажатие 1 кнопки
        key_wc1 = types.InlineKeyboardButton(text='1. Исторические места Омска', callback_data='wc1')
        keyboard.add(key_wc1)

        key_wc2 = types.InlineKeyboardButton(text='2. Прогулка по красивейшим местам Омска', callback_data='wc2')
        keyboard.add(key_wc2)

        key_wc3 = types.InlineKeyboardButton(text='3. Омск Достоевского', callback_data='wc3')
        keyboard.add(key_wc3)

        key_back = types.InlineKeyboardButton(text='Вернуться к меню', callback_data='back')
        keyboard.add(key_back)

        bot.send_message(call.message.chat.id, "Omsk Travel Guide предлагает вам 3 возможных маршрута", reply_markup=keyboard)

    elif call.data == "wc1":  # выбор 1 маршрута
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='1')
        keyboard.add(key_n)
        key_return = types.InlineKeyboardButton(text='Вернуться к выбору', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """Прекрасный выбор! 
«Исторические места Омска» - это маршрут по исторически значимым местам города. Следуя ему, вы сможете увидеть город таким, каким видели его наши предки, познакомитесь с нашей историей. 
Хотите продолжить?""", reply_markup=keyboard)

    elif call.data == "1":  # 1 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='2')
        keyboard.add(key_n)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """1. Омская крепость
Адрес: [Партизанская ул., 5А](https://go.2gis.com/nme6na)

Омская крепость – историко-культурный туристический комплекс, состоящий из реконструированных и восстановленных фрагментов форпоста, с которого началась славная история Омска. Самая первая крепость была построена в начале 18 столетия, вторая, гораздо большей площади – спустя полвека. Одной из ярких достопримечательностей исторического комплекса является дом, в котором некогда жил комендант крепости. На территории комплекса работает музей воинской славы, под открытым небом выставлена боевая техника. Здесь можно посетить тематическую выставку или в кинозале посмотреть документальный фильм о городе.""", parse_mode='Markdown')
        pic = 'https://d1ualep0003st.cloudfront.net/uploads/cards/images/xlarge/3e/34/ff332602-5b1f-11e7-9498-000000000000.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "2":  # 2 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='3')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='1')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """2. Тарские ворота
Адрес: [Спартаковская ул.](https://go.2gis.com/gxjov)

Тарские ворота – один из символов города. Они известны тем, что через них проходил ссыльный Федор Достоевский, который отбывал каторгу в Омском остроге. 
Ворота были построены в 1792 году в качестве входа в Степной бастион крепости, в которой располагался каторжный острог. В 1959 году ворота были уничтожены из-за того, что они не вписывались в окружающий ландшафт, но позже ворота отстроили на новом месте. Новые ворота были построены в 1991 году с некоторыми отклонениями от своего оригинала. Внутри свода вместо двух ниш были сделаны четыре ниши. В одной из ниш была встроена дверь на лестницу, ведущую в караульную комнату площадью 30 квадратных метров.""", parse_mode='Markdown')
        pic = 'https://prigorod.info/images/places/omskaya-oblast/arhitekturnye-ob-ekty/tarskie-vorota-v-omske/3.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "3":  # 3 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='4')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='2')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """3. Успенский собор
Адрес: [Тарская ул., 7](https://go.2gis.com/lt8jo)

Самый важный храм Омска, один из самых красивых и величественных в России, Свято-Успенский кафедральный собор признан уникальным памятником русского зодчества. Церковь была возведена на излете 19 века, в основе – проект знаменитого Санкт-Петербургского Храма Спаса-на-Крови. После октябрьской революции Свято-Успенский кафедральный собор разделил участь большинства культовых сооружений. При восстановлении церкви в 2000-е годы были обнаружены иконы и мощи архиепископа Сильвестра Сибирского, расстрелянного большевиками и канонизированного епархией как новомученик. Сейчас старинные иконы и рака с мощами святого хранятся в здании собора.""", parse_mode='Markdown')
        pic = 'https://tripplanet.ru/wp-content/uploads/europe/russia/omsk/holy-assumption-cathedral.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "4":  # 4 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='5')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='3')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """4. Омский гос академ театр
Адрес: [ул. Ленина, 8А](https://go.2gis.com/advou)

Омский академический театр драмы – старейший драмтеатр в Сибири, принявший первых зрителей в 1875 году. Оно получилось эклектичным, классическая основа декорирована сложными, замысловатыми элементами в стиле барокко. В нишах установлены бюсты великих русских писателей, а фронтон украшает оригинальная скульптура работы чешского мастера Винклера «Крылатый гений» – фигурка ангела, словно парящая в воздухе. Основа репертуара театра – спектакли по классическим произведениям, но есть и современные, экспериментальные постановки. Театр не единожды получал престижные награды.""", parse_mode='Markdown')
        pic = 'http://s3.fotokto.ru/photo/full/218/2183958.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "5":  # 5 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='6')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='4')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """5. Памятник слесарю
Адрес: [ул. Карла Либкнехта, 5](https://go.2gis.com/s0dm3)

Омский памятник слесарю-сантехнику «Степаныч» появился в городе в 1998 году. С момента установки он стал и остается по сей день одной из самых фотографируемых городских скульптур. Памятник сантехнику в Омске является олицетворением уважения горожан к профессии. Памятник представляет собой сантехника, который выглядывает из канализационного люка, на котором лежит разводной ключ. Сантехник в защитной каске положил под подбородок руки и наблюдает городскую суету. Добродушная улыбка Степаныча, его задумчивый взгляд непременно вызывают ответную улыбку. Памятник заслуженно называют самым обаятельным и душевным.""", parse_mode='Markdown')
        pic = 'https://avatars.mds.yandex.net/get-altay/3683342/2a00000175d6f841cc535698d31683b6577d/XXL'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "6":  # 6 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='7')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='5')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """6. Памятник городовому
Адрес: [улица Щербанёва, 2](https://go.2gis.com/x76aqp)

В ноябре 2011 года компания скульптурных композиций, изображающих исторических персонажей, пополнилась новой скульптурой - городовым. Отлитый из бронзы страж порядка высотой 180 сантиметров охраняет перекресток улиц Ленина и Партизанской, напротив Серафимо-Алексеевской часовни, в непосредственной близости от ресторана "Гермелин". Страж порядка выглядит очень реалистично: он экипирован револьвером, шашкой и свистком. Он щегольски подкручивает ус и наблюдает за жизнью на оживленных улицах Омска.""", parse_mode='Markdown')
        pic = 'https://goru.travel/storage/app/uploads/public/5ac/344/4c4/5ac3444c4e73a303574115.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "7":  # 7 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='8')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='6')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """7. Омский краеведческий музей
Адрес: [ул. Ленина, 23 А](https://go.2gis.com/qd735)

Один из первых музеев России. Музей был открыт в 1878 году по инициативе русских учёных, первые выставки состояли из частных пожертвований. В годы Великой Отечественной войны в здании хранились ценные коллекции, вывезенные из музеев городов, оккупированных немцами. За время своего существования музей Омска собрал выдающееся количество экспонатов - более двухсот тысяч. Постоянные выставки, распологаются в 6 залах, рассказывают об истории региона от каменного века до современности, о разнообразной, удивительной природе Омской области. Экспозиции состоят из археологических находок, макетов старинных зданий, чучел, птиц и животных, военных и бытовых орудий, предметов искусства, икон, монет, документов.""", parse_mode='Markdown')
        pic = 'https://must-see.top/wp-content/uploads/2018/11/istoriko-kraevedcheskij-muzej-omska.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "8":  # 8 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='9')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='7')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """8. ТЮЗ
Адрес: [просп. Карла Маркса, 4В](https://go.2gis.com/7f4z2)

ТЮЗ в Омске основан в 1937 году по инициативе омских пионеров. Высокий уровень театральных постановок был задан режиссером Николаем Павловичем Охлопковым, который руководил учреждением, будучи в эвакуации в годы Великой Отечественной войны. С 1967 года ТЮЗ располагается в построенном для него здании на проспекте Карла Маркса напротив Театрального сквера. За прошедшие годы коллективы детского театра в Омске подготовили и показали зрителям более 500 спектаклей. Помимо спектаклей, в омском ТЮЗе проходит множество разноплановых мероприятий: вечера классической музыки и литературы, творческие встречи с коллективом театра, мастер-классы и лекции для школьников, обсуждение театральных постановок, экскурсии по театральному закулисью.""", parse_mode='Markdown')
        pic = 'https://superomsk.ru/images/news/full/2020/12/4c9aef859eb1f8793f292dbd272fc026.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "9":  # 9 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='10')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='8')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """9. Омский кадетский корпус (4 памятника)- старый
Адрес: [ул. Ленина, 26](https://go.2gis.com/qjumhp)

Здание Сибирского кадетского корпуса является одним из наиболее величественных монументальных зданий Омска первой половины XIX века. Обрастая пристройками, это самое крупное учебное заведение города оставалось таким на протяжении более 100 лет. В мае 1813 года в Омске было открыто первое военно-учебное заведение Сибири – Войсковое казачье училище. Двухэтажное, на высоком цоколе с шестиколонным ионическим портиком, являющимся главным акцентом строения, здание привлекает внимание соразмерностью своих деталей и стилевой завершенностью. После бывшей гауптвахты и казармы в крепости – это одно из самых старых двухэтажных кирпичных зданий, сохранившихся до наших дней.""", parse_mode='Markdown')
        pic = 'https://avatars.mds.yandex.net/get-altay/933207/2a00000161cda195bd588d6c1bb9be88c6ed/XXXL'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "10":  # 10 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='11')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='9')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """10. Дом Хлебникова
Адрес: [ул. Почтовая, д. 27 / ул. Сажинская, д. 45](https://go.2gis.com/srkv2g)

Дом был построен по проекту Арсения Хлебникова — общественного деятеля, адвоката и музыканта, которого выселили в Сибирь в 1887 году. В здании не раз проходили литературно-музыкальные вечера, которые посещали выдающиеся люди города: музыкант Виссарион Шебалин, ученый Пётр Драверт, поэт Леонид Мартынов. В доме общей площадью 250 квадратных метров были два кабинета, столовая, гостиная, две детских и одна спальня родителей, кухня и веранда, которая выходила в сад. К северному фасаду здания со стороны кухни были пристроены сени. Кроме того, дом был оформлен резными гирляндами растительного орнамента с элементами модерна.""", parse_mode='Markdown')
        pic = 'https://ic.pics.livejournal.com/irma_wurst/55276046/9922/9922_900.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "11":  # 11 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='12')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='10')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """11. Парк Победы
Адрес: [ул. Андрианова, 3](https://go.2gis.com/e2af7t)

Самая масштабная по площади (более 70 га) благоустроенная зеленая зона Омска – парк культуры и отдыха имени 30-летия ВЛКСМ. Парк был заложен в 1940 году на месте лесного массива как Центральный, а в юбилейный для советской молодежи год получил название, используемое и поныне. Парк – место знаковое, многие омичи в летний воскресный день 1941 года именно здесь услышали горькую и страшную новость о нападении Германии на СССР. Сегодня \"комсомольский\" парк целиком и полностью ориентирован на комфортный отдых и беззаботное времяпрепровождение. Среди густых зарослей парка и вокруг пруда проложены удобные аллеи, работает масса аттракционов.""", parse_mode='Markdown')
        pic = 'https://tripplanet.ru/wp-content/uploads/europe/russia/omsk/park-of-culture-and-leisure-named-after-the-30th-anniversary-of-the-komsomol.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "12":  # 12 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='13')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='11')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """12. Лютеранская церковь Урала
Адрес: [ул. Рождественского, 2/1](https://go.2gis.com/6j9s4d)

Лютеранская церковь Святой Екатерины – единственное здание культового назначения, сохранившееся с 18 века. Построенная на исходе столетия, каменная церковь была уже третьим по счету храмом лютеран в Омске и могла одновременно вместить более 100 человек. В свое время церковь посещали многие государственные чины. Храм принимал прихожан без малого полтора столетия, закрыли его в 1930 году. В 80-х годах прошлого века здание бывшей лютеранской церкви отремонтировали, убрали культовые элементы с фасада и из внутренних помещений. Сейчас здесь хранятся коллекции Музея областного УВД.""", parse_mode='Markdown')
        pic = 'https://tripplanet.ru/wp-content/uploads/europe/russia/omsk/lutheran-church-of-catherine.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "13":  # 13 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='14')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='12')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """13. Казачий собор
Адрес: [ул. Ленина, 27](https://go.2gis.com/x4a30)

Никольский Казачий собор – самый «возрастной» храм Омска, его возвели в начале 19 века. Никольский собор – единственное культовое сооружение в Омске, неразрушенное во время правления Советов. Церковь выполнена в стиле позднего классицизма. Почти столетие церковь владела исторической реликвией – настоящим знаменем войска Ермака. Но в неразберихе гражданской войны стяг похитили, и сейчас выставлена его точная копия. В Казачьем соборе также хранятся святые мощи угодников, в том числе Георгия Победоносца, Серафима Саровского, Сергия Радонежского.""", parse_mode='Markdown')
        pic = 'https://tripplanet.ru/wp-content/uploads/europe/russia/omsk/nikolsky-cossack-cathedral.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "14":  # 14 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='15')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='13')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """14. Мемориал «Вечный огонь»
Адрес: [Центральный округ, Мемориальный сквер Памяти борцов революции](https://go.2gis.com/14qd5)

Мемориальный сквер (Вечный огонь) – одна из достопримечательностей Омска. Создан он был в честь памяти о жертвах Октябрьской революции. Представляет собой целый сквер, который был отдан для этой цели в 1966 году. Но власти не ограничились только лишь облагораживанием данного сквера. Здесь были перезахоронены останки павших, сражавшихся за свободу. Именно поэтому сквер стал мемориальным. 6 ноября 1967 года сквер переименовали в Сквер Борцов Революции. Здесь был установлен Вечный огонь.""", parse_mode='Markdown')
        pic = 'https://avatars.mds.yandex.net/get-altay/4971637/2a0000017cf2f733d3281c428f9f797588f1/XXXL'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "15":  # 15 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='16')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='14')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """15. Площадь Бухгольца
Адрес: [Центр города](https://go.2gis.com/bj6c7)

В месте слияний Оми и Иртыша располагается центральная площадь города. Место историческое, как полагают, именно здесь в 1716 году была заложена крепость – предтеча современного Омска. Площадь носит имя генерала Ивана Бухгольца, по указу Петра I возглавлявшего военную экспедицию, и как раз основавш уютное пространство вдали от шумных магистралей, с ухоженными газонами и мощенными аллеями. Центр площади украшает гигантский (7 м в диаметре) металлический шар «Держава». На его поверхности располагаются панно, иллюстрирующие различные моменты исследования и покорения Сибирской земли.""", parse_mode='Markdown')
        pic = 'https://tripplanet.ru/wp-content/uploads/europe/russia/omsk/buchholz-square.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "16":  # 16 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='17')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='15')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """16. Памятник «труженикам тыла»
Адрес: [Октябрьский округ](https://go.2gis.com/m9zn09)

Памятник труженикам тыла в г. Омске символизирует вечную память омичам, которые в годы Великой Отечественной войны каждый по-своему трудился ради победы. В 2010-м году седьмого мая в торжественной обстановке состоялось открытие этого памятника в честь 65-летия празднования Дня Победы. В центре памятника располагается двусторонняя группа скульптур, которая является прообразом тыловиков Омска в военное время. В эту композицию входят: женщина-мать с младенцем на руках, крестьянка, которая собирается на покос, рабочий оборонного завода, мальчик пастух, девочка, медработник и др. Связующее звено между «деревней» и «городом» - длинный военный эшелон, направляющийся на фронт. Огромные белые крылья в основе памятника.""", parse_mode='Markdown')
        pic = 'https://autotravel.ru/phalbum/91620/120.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "17":  # 17 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='18')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='16')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """17. Скульптура «Люба»
Адрес: [ул. Ленина, 7](https://go.2gis.com/f3l84n)

Скульптура «Люба» в городе Омске является одним из любимых достопримечательностей омичей. Это увековеченное изображение молодой девушки – Любови Гасфорд, которая была супругой Густава Гасфорда – одного из генерал-губернаторов Сибири в 19-м веке. Скульптор запечатлел тот момент, когда Люба (или как в народе еще называют скульптуру Любаша) вышла на прогулку и присела на скамейку. Горожане трепетно и с нежностью относятся к этой скульптуре, поскольку она олицетворяет собой женскую красоту и одновременно скромность, а также показывает частичку прошлого города Омска.""", parse_mode='Markdown')
        pic = 'https://avatars.mds.yandex.net/get-zen_doc/5324612/pub_60eeffa666960a55e1cb8617_60ef009266960a55e1ce588d/scale_1200'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "18":  # 18 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='19')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='17')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """18. Дом со шпилем
Адрес: [просп. Карла Маркса, 29](https://go.2gis.com/13zmc)

В середине прошлого века многоэтажка была своего рода парадными воротами Омска. Венчала перекресток Маркса и Масленникова, которая в те годы называлась Перевозной. По задумке автора на этом месте должен был возвышаться целый архитектурный ансамбль — у Дома со шпилем мог появиться близнец.""", parse_mode='Markdown')
        pic = 'https://avatars.mds.yandex.net/get-altay/2714499/2a00000171831f91ecf215d2faff70c9135c/XXL'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "19":  # 19 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='20')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='18')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """19. Каланча
Адрес: [Интернациональная ул., 41, корп. 2](https://go.2gis.com/sfrbk)

Пожарная каланча – колоритная достопримечательность Омска, своеобразный символ города. Конструкция из красного кирпича была построена в начале прошлого века, причем на том же месте, где ранее располагалась деревянная вышка. Назначение каланчи – следить с высоты за ситуацией в городе и оперативно реагировать на пожары, что особо актуально при массовой деревянной застройке. Каланча использовалась по прямому назначению до середины прошлого столетия. Сейчас это исторический и архитектурный памятник, внутри которого располагается музей. Экспозиции посвящены пожарной охране и рассказывают историю башни.""", parse_mode='Markdown')
        pic = 'https://tripplanet.ru/wp-content/uploads/europe/russia/omsk/fire-tower.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "20":  # 20 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='21')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='19')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """20. Здание гауптвахты
Адрес: [Партизанская ул., 14](https://go.2gis.com/kloov)

По ходу строительства новой омской крепости в ней стали появляться не только военные здания, но и гражданские. И наверное одним из первых подобных строений стало здание Гауптвахты, построенное в 1781 году. В свое время она являлось одним из самых красивых и больших каменных зданий в городе. В оригинальном виде здания присутствовала колоннада из шести колонн, соединяющая боковые выступы. Которая в последствии была разобрана. В помещениях гауптвахты изначально располагался караул крепости. Сейчас в этом здании располагается областной военкомат.""", parse_mode='Markdown')
        pic = 'https://olxlo.ru/images/stories/omsk-tort/gauptvahta.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "21":  # 21 достопримечательность
        key_end = types.InlineKeyboardButton(text='Закончить', callback_data='end')
        keyboard.add(key_end)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='20')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """21. ЖД вокзал
Адрес: [ул. Леконта, 1](https://go.2gis.com/4chcw)

Омский ЖД вокзал был построен к 1896 году, в то же время, когда велось строительство Транссибирской магистрали. Это было одноэтажное здание с одним корпусом, таким сооружение просуществовало до 1914 года. С началом первой мировой войны пассажиропоток увеличился, активизировалась военная промышленность, и нагрузка на транспортную систему возросла. К 1958 реконструкция была завершена, и у вокзала появилось 3 этажа, изменился и внешний вид вокзала, возросло число направлений электропоездов. В 2004 году рядом с главным зданием построили второй корпус – пригородный вокзал.""", parse_mode='Markdown')
        pic = 'https://vokzalomsk.ru/wp-content/uploads/omsk.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "wc2":  # выбор 2 маршрута
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='22')
        keyboard.add(key_n)
        key_return = types.InlineKeyboardButton(text='Вернуться к выбору', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """Прекрасный выбор! 
«Прогулка по красивейшим местам Омска» – это маршрут, созданный для того, чтобы вы смогли насладиться красотой нашего города и, возможно, узнать его с новой стороны. По ходу маршрута вы сможете сделать красивые фотографии или просто наблюдать одни из самых эстетичных мест города. 
Хотите продолжить?""", reply_markup=keyboard)

    elif call.data == "22":  # 22 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='23')
        keyboard.add(key_n)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """1. Птичья гавань
Адрес: [Енисейская улица, дом 1 корпус 2](https://go.2gis.com/yie22)
        
Птичья гавань — природный парк, расположенный в черте города Омска, особо охраняемая территория, наделённая статусом объекта регионального значения. Природно-антропогенное сообщество, имеющее важное значение для экологического каркаса города. Находится на пути миграции птиц, во время осенних перелётов на водоёмах останавливается до трёх тысяч особей. Птичья гавань является объектом исследований омских учёных и, по планам губернатора Омской области, должна стать визитной карточкой города.""", parse_mode='Markdown')
        pic = 'http://rasfokus.ru/images/photos/medium/aabbf9c1bc22a31f863978a56a7d1452.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "23":  # 23 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='24')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='22')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """2. Улица Чокана Валиханова
Адрес: [улица Чокана Валиханова](https://go.2gis.com/3e3552)
        
Улица названа в честь Чокана Валиханова – великого казахского ученого, поэта, писатела и исследователя, выпускника Омского кадетского корпуса. Главная достопримечательность улицы — арт-конструкции из стекла, которые Омичи прозвали кристаллами. Днем они отражают свет, а вечером красиво подсвечиваются, внутри них стоят большие планшеты, где можно узнать всю информацию о памятниках и достопримечательностях города Омска. А еще есть два очень интересных фонтана: водопады, стекающие по граням многогранников. В темное время суток все подсвечивается, а кристаллы с планшетами меняют цвет. Очень много лавочек для отдыха, зелени и цветов. Заканчивается она прекрасной смотровой площадкой, откуда открываются живописные виды на реку Иртыш.""", parse_mode='Markdown')
        pic = 'https://domoos.ru/images/goroda/places/omsk/ulica-valihanova.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "24":  # 24 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='25')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='23')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """3. Иртышская набережная
Адрес: [улица Иртышская Набережная](https://go.2gis.com/xiq9c)
        
Мощеная Иртышская набережная — одна из самых популярных прогулочных улиц в Омске. Пешеходная ее часть протянулась вдоль реки Иртыш и имеет в длину почти 4 километра. В прошлом веке ее название было — улица Береговая. Живописные панорамы, открывающиеся с набережной, делают ее основным местом посещения для прогулок и совершения памятных фотографий жителями города, молодоженами и, конечно же, гостями города. Вдоль пешеходной улицы, параллельно ей, проходит автомобильная дорога с одноименным названием. Протянулась она от улицы Чкалова (в районе Куйбышевского пляжа) до улицы Рождественского.""", parse_mode='Markdown')
        pic = 'https://must-see.top/wp-content/uploads/2018/11/irtyshskaya-naberezhnaya-v-omske.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "25":  # 25 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='26')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='24')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """4. Улица Ленина
Адрес: [улица Ленина](https://go.2gis.com/dwkwo)
        
Улица Ленина — центральная улица города Омска, расположенная в районе исторической застройки. Проходит от Соборной площади через Юбилейный мост до ул. Маяковского параллельно проспекту К. Маркса. Здесь сохранился единственный в своём роде архитектурный ансамбль конца XIX — начала XX вв., получивший статус исторического памятника федерального значения и являющийся достопримечательностью города. В праздничные дни движение транспорта по улице Ленина перекрывается для народных гуляний.""", parse_mode='Markdown')
        pic = 'https://kraskimira-nsk.ru/wp-content/uploads/2020/09/omsk_ul-lenina.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "26":  # 26 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='27')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='25')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """5. Площадь Бухгольца
Адрес: [площадь Бухгольца](https://go.2gis.com/bj6c7)
        
Площадь Бухгольца - центральная площадь Омска, место прогулок и отдыха горожан. Она расположена в самом центре города, вблизи от речного вокзала. История площади связана с историей Омска, именно здесь в начале XVIII столетия была заложена крепость. От крепости со временем не осталось никаких следов. Во время Гражданской войны на месте сегодняшней площади во время пребывания в Омске штаба А.В. Колчака была установлена радиомачта. Это еще один любопытный сюжет из истории, ведь обслуживанием этой радиомачты занимался инженер Зворыкин, прославившийся тем, что во время эмиграции в Америку, изобрел телевидение. Мачта была снесена коммунистами, но история осталась.""", parse_mode='Markdown')
        pic = 'https://pbs.twimg.com/media/Dn7bPMPXcAAJHMx.jpg:large'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "27":  # 27 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='28')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='26')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """6. Омская крепость
Адрес: [Партизанская, 5а](https://go.2gis.com/g88sp)
        
Омская крепость — сторожевое укрепление Сибирской линии, возведенной в XVIII—XIX веках для защиты южных границ от набегов кочевников. С постройки первой крепости, воздвигнутой в 1716 году в виду двух редутов, началась история города Омск. Благодаря наличию крепости Омск стал главным городом Западной Сибири.""", parse_mode='Markdown')
        pic = 'http://1.bp.blogspot.com/-Y6F8-Yi04uQ/Tk1Fi4fFivI/AAAAAAAACUU/zni_oZOSRJ8/s1600/DSC_0180.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "28":  # 28 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='29')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='27')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """7. Библиотека им Пушкина
Адрес: [улица Красный Путь, 11](https://go.2gis.com/ys6s0)
        
Омская государственная областная научная библиотека имени А. С. Пушкина — публичная библиотека в Омске, ныне является главной научной библиотекой области. Она основана Омской городской думой в 1899 г. Открыта для читающей публики в 1907 г. Примечательно, что открытие читального зала ("читальни") состоялось 3 февраля (21 января по ст. ст.) 1907 г. накануне выборов во II Государственную Думу, когда в Омске кипели нешуточные предвыборные страсти и складывались весьма непростые отношения в городском общественном управлении.""", parse_mode='Markdown')
        pic = 'https://vibirai.ru/image/603413.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "29":  # 29 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='30')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='28')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """8. ПКиО им 30 лет ВЛКСМ
Адрес: [Масленникова, 136](https://go.2gis.com/66v1rx)
        
Парк культуры и отдыха им. 30-летия Победы — парк города Омска, расположенный на Левобережье Иртыша рядом с Ленинградским мостом и через дорогу от природного парка «Птичья гавань». С февраля 2015 года имеет статус особо охраняемой природной территории местного значения. Площадь парка вместе с Кировским островом составляет 268 га. Значительную её часть занимает единый зелёный массив, также имеется комплекс памятников, включая Вечный огонь и памятник «Мать-сибирячка».""", parse_mode='Markdown')
        pic = 'https://afisha-omsk.ru/media/events/1428922908_park-kultury-i-otdyha-im-30-letiya-vlksm3.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "30":  # 30 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='31')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='29')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """9. Омский гос муз театр
Адрес: [10 лет Октября, 2](https://go.2gis.com/hnscl2)
        
Омский государственный музыкальный театр ведет свою историю с 1946 года, когда распоряжением Совета Народных Комиссаров РСФСР было принято решение об организации в городе областного театра музыкальной комедии. Сегодня афиша театра богата спектаклями самых разнообразных жанров как классического, так и современного искусства: опера, балет, оперетта, мюзикл, концерт-диалог, театрализованная феерия, рок-балет, партнерские проекты с приглашенными артистами из других городов России и стран дальнего зарубежья.""", parse_mode='Markdown')
        pic = 'https://assets.change.org/photos/1/sd/vp/ULsdvpAhtPzGPwN-1600x900-noPad.jpg?1489386166'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "31":  # 31 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='32')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='30')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """10. Омская филармония
Адрес: [Партизанская, 4](https://go.2gis.com/2kdyb)
        
Омская филармония – инициатор и организатор крупных культурных форумов. При поддержке Правительства Омской области проходят Сибирский международный фестиваль органной музыки, в рамках которого выступают ведущие органисты Европы и мира, Фестиваль Новой музыки, где звучат симфонические новинки, Межрегиональный детский фестиваль-конкурс русской песни имени Е.В. Калугиной. С 2009 года молодые исполнители из разных стран мира принимают участие в Международном конкурсе скрипачей им. Ю.И. Янкелевича.""", parse_mode='Markdown')
        pic = 'https://travelask.ru/system/images/files/001/013/259/wysiwyg/зал.jpg?1514454992'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "32":  # 32 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='33')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='31')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """11. Музей искусств им Врубеля
Адрес: [Ленина, 3](https://go.2gis.com/2utow)
        
Омский областной музей изобразительных искусств имени М.А. Врубеля — один из крупнейших художественных музеев Сибири, был основан в 1924 г. как картинная галерея при Западно-Сибирском краевом музее при содействии первого директора музея Ф.В. Мелёхина.""", parse_mode='Markdown')
        pic = 'https://must-see.top/wp-content/uploads/2021/04/muzey-izobrazitelnyh-iskusstv-imeni-m.-a.-vrubelya.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "33":  # 33 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='34')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='32')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """12. Музей Белова
Адрес: [Чокана Валиханова, 10](https://go.2gis.com/mn3sy)
        
Дом-музей Белова в Омске посвящен творчеству сибирского пейзажиста Кондратия Петровича Белова. От многих галерей с холодными залами и пыльными экспонатами его отличает необычайный уют. Многие посетители в отзывах пишут, что после музея остается ощущение как будто ты побывал в гостях у радушных хозяев.
Музей располагается в историческом деревянном доме, напоминающем сказочный теремок. Дом выделяется среди омской застройки: резное кружево на наличниках со славянским орнаментом, небольшой мезонин, башенки, нагромождение ярусов, которое смотрится не нелепо, а по-сказочному.""", parse_mode='Markdown')
        pic = 'https://afisha-omsk.ru/media/events/3686bcd74d8946a09af9a6b8ca79779c.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "34":  # 34 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='35')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='33')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """13. Музей воинской славы
Адрес: [Таубе, 7](https://go.2gis.com/ltv9yl)
        
К 40-летию Победы в Великой Отечественной войне по инициативе объединённого историко-литературного музея и секции Комитета ветеранов Великой Отечественной войны в здании бывшего штаба 178-й Кулагинской Краснознаменной стрелковой дивизии по улице Таубе, 7 был открыт филиал Омского государственного историко-краеведческого музея «Музейный комплекс воинской славы омичей». На карте города появился новый музей Отечественной военной истории.""", parse_mode='Markdown')
        pic = 'https://culttourism.ru/data/photos/7/d/7dcf6cabc8e1e135a0ee83ce1ae29b61.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "35":  # 35 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='36')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='34')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """14. Крестовоздвиженский собор
Адрес: [Партизанская, 16](https://go.2gis.com/fgearm)
        
Крестовоздвиженский собор – это второй по возрасту православный храм Омска, сохранившийся в городе с дореволюционных времен. Храм располагается в центральной части города на пересечении трех улиц - Третьяковской, Тарской и Рабиновича. Инициатором строительства собора в 1858 г. стал генерал-губернатор Западной Сибири и Войсковой Наказной Атаман Сибирского казачьего войска Г. Х. Гасфорд.""", parse_mode='Markdown')
        pic = 'https://must-see.top/wp-content/uploads/2020/01/krestovozdvizhenskii-sobor.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "36":  # 36 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='37')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='35')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """15. Серафимо-Алексеевская часовня
Адрес: [Ленина, 18а](https://go.2gis.com/4p92pv)
        
В 1907 году в Омске у Железного (сегодня Юбилейного) моста через Омь в честь рождения наследника престола цесаревича Алексея была построена каменная часовня с шатровым завершением. Ей дали имя Серафима Саровского Чудотворца и Святителя Алексия. Архитектурный проект, автором которого по одним данным считается выдающийся сибирский архитектор А.Д. Крячков, по другим – петербургский зодчий А.И. фон Гоген, несет на себе черты стиля ярославского зодчества.""", parse_mode='Markdown')
        pic = 'http://vomske.ru/images/tini/2019_10/e9945be3cfadb12c9af8798f4d32fda0_1024.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "37":  # 37 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='38')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='36')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """16. Дендрологический сад им Гензе
Адрес: [улица Красный Путь, 86](https://go.2gis.com/2m5c7)
        
Дендрологический парк заложен в 1948 г. по проекту А.А. Ануфриева как парково-оранженейное хозяйство. Все озеленение, которое существует сегодня в городе Омске, родом из совхоза "Декоративные культуры", так раньше назывался дендропарк. Благодаря таланту и удивительному трудолюбию агронома-селекционера Г.И. Гензе на улицах Омска и других сибирских городов появились серебристые пирамидальные тополя – тополя Гензе, голубые ели, махровая сирень форма курчавая и другие растения.""", parse_mode='Markdown')
        pic = 'https://s12.stc.all.kpcdn.net/share/i/12/11993578/wr-960.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "38":  # 38 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='39')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='37')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """17. Сквер им Дзержинского
Адрес: [Сквер им. Дзержинского](https://go.2gis.com/43614)
        
Сквер имени Дзержинского является крупнейшим парком в историческом центре Омска. Здесь же находится художественный музей имени Врубеля. Когда-то здесь была Базарная площадь, но в 1944 году было принято решение о создании парка. В центре сквера Дзержинского в 1958 году был построен трёхъярусный фонтан в виде вазы. В 2015 году к 300-летию Омска сквер полностью преобразился. Во многих местах установлены монументы и скульптуры, высажены деревья и цветы. Зимой в сквере проводят выставку ледяных скульптур.""", parse_mode='Markdown')
        pic = 'https://omskzdes.ru/storage/c/2018/06/26/1530009993_859260_02.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "39":  # 39 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='40')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='38')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """18. ПКиО «Зеленый остров»
Адрес: [Старозагородная Роща, 10/1](https://go.2gis.com/vi1ahg)
        
Парк Зеленый остров в городе Омске располагается на улице с интересным названием Старозагородная Роща. Примечательно, что этот красивый парк, который по праву называется зеленым благодаря насыщенной растительности, находится на берегу речки Иртыш. Поэтому здесь можно как любоваться насаждениями, так и водной гладью реки. Открытие «Зеленого острова» датируется августом 1985-го года, а его внушительная территория равняется 72-м гектарам. Это парк действительно создан для прекрасного времяпрепровождения и душевного отдыха местных жителей и гостей города. Сюда родители приводят своих малышей покататься на аттракционах, которых здесь масса совершенно на любой вкус. Присутствуют также специально отведенные дорожки для тех, кто предпочитает катание на велосипедах и любителей роликов. По утрам и вечерам это место облюбовали спортсмены-бегуны.""", parse_mode='Markdown')
        pic = 'https://i5.photo.2gis.com/images/branch/2/281475009210713_bb18.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "40":  # 40 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='41')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='39')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """19. Бульвар Победы
Адрес: [Бульвар Победы](https://go.2gis.com/jcf8r)
        
Бульвар Победы — один из важнейших, знаковых участков центральной части города Омска, — создан в 1960 году, одновременно с возведением набережной на реке Иртыш и массовым строительством жилья на намывных территориях. Ранее на месте пешеходной аллеи располагались бараки и железнодорожная ветка. В мае 1985 года в рамках подготовки к празднованию 40-летия Победы в Великой Отечественной войне 1941 1945 гг. был торжественно открыт мемориальный комплекс «Слава Героям», ставший доминантой бульвара.""", parse_mode='Markdown')
        pic = 'https://mtdata.ru/u24/photo3211/20643137730-0/original.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "41":  # 41 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='42')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='40')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """20. Станция юннатов (зоопарк)
Адрес: [Маршала Жукова, 109/1](https://go.2gis.com/2jvlg)
        
Омская областная станция юных натуралистов – одно из старейших внешкольных учреждений, имеющая большой опыт и традиции в области эколого-биологического образования и воспитания детей. В 1923 году в городе Омске начали работу первые юннатские кружки. На улице Большая Ивановская стоял маленький деревянный домик под № 15, состоявший из 5 небольших комнат, который с трудом вмещал семилетнюю школу имени КИМ. Именно здесь и начиналась работа юннатского кружка.""", parse_mode='Markdown')
        pic = 'https://img.tourister.ru/files/1/6/0/2/1/5/1/2/original.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "42":  # 42 достопримечательность
        key_end = types.InlineKeyboardButton(text='Закончить', callback_data='end')
        keyboard.add(key_end)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='41')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """21. Дом Колчака
Адрес: [улица Иртышская Набережная, 9](https://go.2gis.com/4z2sn)
        
Находящийся в центре города Омска особняк купца Батюшкова был построен в начале двадцатого века. Второе название — Дом Колчака, напрямую связано с проживанием здесь в 1919 году Александра Колчака. Здесь располагалась его резиденция в годы Гражданской войны, и происходило командование белогвардейцами. Омск в годы Гражданской был провозглашен третьей столицей. И он по факту был столицей Белой России во главе с Александром Колчаком. В годы Гражданской войны здание купца Батюшкова было частично разрушено в связи с покушением на Александра Колчака. Но позже было отреставрировано городскими властями. На сегодняшний день это одно из красивейших исторических зданий города Омска.""", parse_mode='Markdown')
        pic = 'https://avatars.mds.yandex.net/get-zen_doc/1328466/pub_5b8783e3fa946400aa8e7a81_5b8784b604056e00aa464a68/scale_1200'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "wc3":  # выбор 3 маршрута
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='43')
        keyboard.add(key_n)
        key_return = types.InlineKeyboardButton(text='Вернуться к выбору', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """Прекрасный выбор! 
    «Омск Достоевского» - это маршрут по местам города, связанным с Великим писателем. Следуя ему, вы сможете пройти по тем местам, где был ходил Он, увидеть места, вдохновлявшие писателя на во время ссылки в Сибирь. 
    Хотите продолжить?""", reply_markup=keyboard)

    elif call.data == "43":  # 43 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='44')
        keyboard.add(key_n)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """1. Драмтеатр
Адрес: [644043, г. Омск, ул. Ленина, д. 8а](https://go.2gis.com/4nler)
        
Омский академический театр драмы – старейший театр города Омска, основан в 1874 году. Нынешнее театральное здание построено в 1905 году по проекту архитектора И.Г.Хворинова. Омский драматический – театр с богатой историей и традициями. В его стенах работали и работают великие артисты, режиссёры, художники. Сегодняшняя труппа Омского академического отличается уникальными качествами – в едином, хорошо сработанном и слаженном ансамбле слышен голос каждого таланта, каждой яркой, ни на кого не похожей личности, мастерство передается от одного театрального поколения к другому, «заражая» театральную молодежь особой атмосферой Омской драмы. В течение многих десятилетий Омский театр драмы признают одним из самых интересных и ярких провинциальных театров в России.""", parse_mode='Markdown')
        pic = 'https://img-fotki.yandex.ru/get/195518/156034130.19/0_1dfaee_33fbbbfe_XXL.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "44":  # 44 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='45')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='43')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """2. Памятник «Крест несущий»
Адрес: [Центральный округ, Омск](https://go.2gis.com/wfussv)
        
Памятник «Крест несущий» установлен в сквере около Омского государственного академического театра драмы в 2000 году. Возведен он в память о том, что в 1850 – 1854 годах в Омском остроге отбывал каторгу великий русский писатель Ф.М. Достоевский. Авторы памятника – скульптор А. Капралов и архитектор Ю.А. Захаров. Это единственная скульптура Ф.М. Достоевского, созданная методом сварки. В одном только лице писателя около 500 сваренных кусочков металла. Скульптура стоит на небольшом плинте, без высокого пьедестала. Тяжелый крест придавливает своим весом вертикаль фигуры, но это не тяжесть извне, крест составляет с телом некое единое целое. Это груз самого себя, своих ошибок и привычек.""", parse_mode='Markdown')
        pic = 'https://s9.stc.all.kpcdn.net/share/i/4/1364703/inx960x640.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "45":  # 45 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='46')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='44')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """3. Тарские ворота
Адрес: [улица Граничная, 2 а](https://go.2gis.com/atmcy)
        
Тарские ворота – это один из символов города. На многих марках и открытках Омска изображены именно они. Свою историю Тарские ворота начинают в 1792 году, они были построены на северной крепостной линии. Ворота были главным входом в Степной бастион Омской крепости, в котором находился каторжный острог. В те времена Омск, по сути, и был всего лишь каторжным острогом, да корпусом военных, которые его охраняли. В Омск был сослан Достоевский, во время его четырехлетней ссылки он каждый день проходил через Тарские ворота. В 1959 году советская власть решила, что символ старины Омску ни к чему, ворота были снесены, в 1991 году их отстроили вновь, по сохранившимся фотографиям.""", parse_mode='Markdown')
        pic = 'https://susanintop.com/wp-content/uploads/2019/01/1Тарские-ворота.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "46":  # 46 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='47')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='45')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """4. Тобольские ворота
Адрес: [набережная Тухачевского](https://go.2gis.com/lcgpg8)
    
Через Тобольские крепостные ворота водили каторжников на берег Иртыша, где они работали. Бывшие казармы и инженерная мастерская ныне отреставрированы. Из крепости можно было выйти и через Иртышские ворота, те вели к пристани. В Омске Достоевскому приходилось бывать в военном госпитале по улице Скорбященской (ныне Гусарова). Сейчас на том месте находится военная часть. Бывал писатель в доме коменданта крепости Алексея Фёдоровича де Граве. Это был смелый человек, участник Отечественной войны 1812 года и заграничных походов Русской армии. В одном из писем брату Фёдор Михайлович напишет – «комендант был очень порядочный».""", parse_mode='Markdown')
        pic = 'https://posibiri.ru/wp-content/uploads/2021/07/030721122333.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "47":  # 47 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='48')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='46')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """5. Воскресенский собор
Адрес: [улица Партизанская д.16](https://go.2gis.com/c4fgk)
    
Воскресенский собор стал первым каменным зданием города, построенным на месте обветшавшей деревянной церкви. Его возведением руководили тобольские ямщики братья Иван и Козьма Черепановы – личности поистине легендарные. Воскресенский собор возводили в составе Омской крепости. Это был военный храм. Величественный собор призван был обозначить освоенность территории Сибири христианской цивилизацией. Факт заложения церкви в день Воскресения Христова в 1769 году, ставший престольным праздником собора, определил важность Омской крепости как оплота христианской культуры. Историю Воскресенского собора по крупицам собрали участники общественного проекта «Омская земля» под руководством Даниила Лапина""", parse_mode='Markdown')
        pic = 'https://img-fotki.yandex.ru/get/892397/239346502.87/0_18caf7_c6c9fa84_XXL.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "48":  # 48 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='49')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='47')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """6. Ул. Гусарова, 4 ( Бывшее здание госпиталя)
Адрес: [Ул. Гусарова, 4](https://go.2gis.com/9l0wm)
        
Ул. Гусарова, 4 ( Бывшее здание госпиталя). Оно не было признано памятником архитектуры, как те здания, о которых мы писали ранее, но его историческая ценность неоспорима. В бывших летних арестантских палатах на Гусарова, построенных в 1823 году, во время каторги в Омске лечился русский писатель Фёдор Достоевский.""", parse_mode='Markdown')
        pic = 'https://sun9-34.userapi.com/c853628/v853628700/1dfbaa/8-mH8OmWiIM.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "49":  # 49 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='50')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='48')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """7. Гауптвахты здание
Адрес: [Партизанская ул., 14](https://go.2gis.com/2z91e)
        
ГАУПТВАХТЫ ЗДАНИЕ, Омск, памятник архитектуры федер. значения. Построено в 1781–84. Самое старое из сохранившихся строений Омска, заложено в сев. части плац-парада 2-й Омской крепости. Яркий образец позднего барокко в Сибири. Два этажа четко разграничены выступающим карнизом, здание прямоугольное в плане с выступающими боковыми ризалитами и треугольным фронтоном, искаженным поздними перестройками (первонач. центр. часть имела портик с 6 колоннами). 1-й этаж отделан рустовкой, 2-й – пилястрами и барочными наличниками. Над центром здания – башня деревян., 4-гранная, с часами, колоколом, бочкообраз. куполом и шпилем (разобрана в 1938). Поначалу в здании размещались комендантское правление и крепостной караул. В 1789–1804 на 2 этаже располагалась Азиатская школа – 1-е учеб. заведение города. Позже гауптвахта использовалась для содержания преступников. В 1856–88 здесь находились арестованные областники С.С. Шашков, Г.Н. Потанин, Н.М. Ядринцев, Н.С. Щукин и др. В наст. время здание отдано под военкомат.""", parse_mode='Markdown')
        pic = 'http://bsk.nios.ru/sites/bsk.nios.ru/files/fotogalereya/gaupvahty_zdanie_omsk.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "50":  # 50 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='51')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='49')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """8. Литературный музей имени Ф.М. Достоевского
Адрес: [ул. Достоевского,1](https://go.2gis.com/ji2i3)
    
Музей располагается в историческом здании — доме комендантов Омской крепости (1799 года постройки). В этом доме жил Алексей Федорович де Граве, последний комендант крепости, оказывавший каторжнику Достоевскому особое покровительство. Экспозиция музея размещается в 9 залах и состоит из 2 разделов: «Ф.М. Достоевский и Сибирь» и «Писатели-омичи».""", parse_mode='Markdown')
        pic = 'https://www.pulslive.com/upload/medialibrary/688/Омский%20литературный%20музей%20имени%20Ф.М.%20Достоевского.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "51":  # 51 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='52')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='50')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """9. Памятник Достоевскому
Адрес: [перекресток улиц Партизанская и Спартаковская в исторической части Омска](https://go.2gis.com/nrtp53)
    
Памятник Достоевскому в Омске установлен в створе ул. Спартаковской и Партизанской 12 ноября 2001 года. Одной из знаковых достопримечательностью города название которого расшифровывается как Отдаленное Место Ссылки Каторжников (ОМСК) - это факт прибывание в ссылки Достоевского, предполагается что здесь он написал знаменитый роман "Приступление и Наказание". На скульптуре изображен Достоевский который прогуливается по крепости в которой его содержали ( если верить историкам это реальный маршрут выгула заключенных). Он идет от Тарских ворот к баракам.""", parse_mode='Markdown')
        pic = 'https://i0.photo.2gis.com/images/geo/2/281475019642191_7199.jpg'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "52":  # 52 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='53')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='51')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """10. Галерея «Квадрат»
Адрес: [ул. Победы, 1А, Омск](https://go.2gis.com/2o42k)
    
Галерея «КвадраТ» открылась 12 апреля 2003 года. Расположена в центре города между Петропавловской крепостью и крейсером «Аврора» — символами двух важнейших событий истории России. Галерея представляет искусство разного времени, начиная с творчества художников послевоенного периода, экспонируя традиционные виды и формы искусства, а также показывает творчество художников новых течений.""", parse_mode='Markdown')
        pic = 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0c/7f/11/39/photo0jpg.jpg?w=1200&h=1200&s=1'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "53":  # 53 достопримечательность
        key_n = types.InlineKeyboardButton(text='Продолжить', callback_data='54')
        keyboard.add(key_n)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='52')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """11. Корпус мед.академии ( бывшее здание военного суда)
Адрес: [ул. Ленина, д. 12](https://go.2gis.com/5o4fu)
        
На Спартаковской улице, которая упирается в Выставочный сквер, находится здание бывшего военного суда. Оно было построено в середине 19 века. Архитектура здания выполнена в рамках классицизма, но поскольку дом предназначался под военный объект Омской крепости, то его декор и формы функциональны, лаконичны и просты. С 1982 года здесь, в доме № 9 по улице Спартаковской, располагается 6 корпус Омской медицинской академии, где находится кафедра гистологии и эмбриологии, имеющая длинную и славную историю. На первом этаже здания находится музей, в котором представлены микроскопы 19-20 веков. Федор Михайлович Достоевский, отбывая каторгу в Омской крепости, был задействован в штукатурных работах в помещении военного суда""", parse_mode='Markdown')
        pic = 'https://im0-tub-ru.yandex.net/i?id=051ea58ece5da70192436d411ad1a3fe-l&n=13'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "54":  # 54 достопримечательность
        key_end = types.InlineKeyboardButton(text='Закончить', callback_data='end')
        keyboard.add(key_end)
        key_p = types.InlineKeyboardButton(text='Вернуться назад', callback_data='41')
        keyboard.add(key_p)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу', callback_data='rc1')
        keyboard.add(key_return)
        bot.send_message(call.message.chat.id, """12. Городской музей «Искусство Омска» (Бывшая инженерная мастерская Омской крепости, именно здесь сначала заковали Достоевского в кандалы по прибытии на омскую каторгу, а затем и расковали.)
Адрес: [ул. Партизанская, 5а, литера М](https://go.2gis.com/7xriu)
    
Городской музей «Искусство Омска» (ГМИО) создан решением Омского городского Совета № 75 от 21 февраля 1991 года. Появление нового музея подводило итог предшествующему периоду интенсивной художественной жизни города, синтезируя достижения официального и неформального направлений искусства. Но в то же время открывало новую страницу истории города, институционально закрепляя положение омского художника в системе городской жизни.""", parse_mode='Markdown')
        pic = 'https://avatars.mds.yandex.net/get-altay/1420183/2a0000016763567be82848fa1be29e25a5ca/XXL'
        bot.send_photo(call.message.chat.id, pic, reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "c2":  # отзыв на нажатие 2 кнопки
        key_back = types.InlineKeyboardButton(text='Вернуться к выбору', callback_data='back')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Omsk Travel Guide – бот-путеводитель для жителей и гостей города Омска. Программа позволяет выбрать наиболее известные и понравившиеся достопримечательности, предложенные разработчиками, основываясь на местоположении пользователя. Бот дает возможность увидеть изображение, адрес и краткую аннотацию выбранных объектов.", reply_markup=keyboard)

    elif call.data == "c3":  # отзыв на нажатие 3 кнопки
        key_back = types.InlineKeyboardButton(text='Вернуться к выбору', callback_data='back')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, "Группа БИТ-211. Лидер группы: Краля Алексей - участие в принятии креативных решений, разработка блоков приложения, создание календарного плана работ; Тестировщик: Сучкова Алина - участие в принятии креативных решений, разработка плана тестирования, тестирование приложения, выявление багов; Аналитик: Нагний Екатерина - создание и проработка технического задания, участие в принятии креативных решений; Разработчики: Сизов Данила - главный разработчик; Устименко Любовь - участие в принятии креативных решений, разработка программы; Поречин Роман - разработка программы; Крючков Андрей - разработка программы.", reply_markup=keyboard)

    elif call.data == "back":  # кнопка возврата
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == "end":  # кнопка завершения
        key_back = types.InlineKeyboardButton(text='Продолжить использование', callback_data='back')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, '«Очень жаль, что вы решили уйти от нас, надеемся на ваше возвращение', reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)

    elif call.data == "rc1":  # кнопка возврата к выбору маршрута
        key_wc1 = types.InlineKeyboardButton(text='1. Исторические места Омска', callback_data='wc1')
        keyboard.add(key_wc1)

        key_wc2 = types.InlineKeyboardButton(text='2. Прогулка по красивейшим местам Омска', callback_data='wc2')
        keyboard.add(key_wc2)

        key_wc3 = types.InlineKeyboardButton(text='3. Омск Достоевского', callback_data='wc3')
        keyboard.add(key_wc3)

        key_back = types.InlineKeyboardButton(text='Вернуться к меню', callback_data='back')
        keyboard.add(key_back)

        bot.send_message(call.message.chat.id, "Omsk Travel Guide предлагает вам 3 возможных маршрута", reply_markup=keyboard)
        for id in (call.message.message_id - 1, call.message.message_id):
            bot.delete_message(call.message.chat.id, id)


bot.infinity_polling()