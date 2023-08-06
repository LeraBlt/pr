import telebot
from telebot import types, TeleBot

bot: TeleBot = telebot.TeleBot('6153432051:AAFZrE-r4My1jiYLbRpGPMcf7QoVVsY1Mk0')


@bot.message_handler(commands=['start'])
def start_message(message):
    name = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, name, parse_mode='html')
    bot.send_message(message.chat.id, 'Привет меня зовут Подручный, я помогу тебе подготовться к ЕГЭ по русскому языку', parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    st = types.KeyboardButton('Структура')
    ex = types.KeyboardButton('Теория')
    markup.add(st, ex)
    bot.send_message(message.chat.id, "Тебя интерисует структура или теория к каждому заданию?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Структура':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        k = types.KeyboardButton('Кодификатор')
        s = types.KeyboardButton('Спецификация')
        d = types.KeyboardButton('Демоверсия')
        markup.add(k, s, d)
        bot.send_message(message.chat.id, "Кодификатор, спецификация или демоверсия",
                         reply_markup=markup)
    elif message.text == 'Кодификатор':
        ko = open('kodif.pdf', 'rb')
        bot.send_document(message.chat.id, ko)
        menu(message)
    elif message.text == 'Спецификация':
        sp = open('spez.pdf', 'rb')
        bot.send_document(message.chat.id, sp)
        menu(message)
    elif message.text == 'Демоверсия':
        de = open('demo.pdf', 'rb')
        bot.send_document(message.chat.id, de)
        menu(message)
    elif message.text == 'Теория':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        z = types.KeyboardButton('Теория к каждому заданию')
        slo = types.KeyboardButton('Словари')
        soch = types.KeyboardButton('Сочинение')
        ot= types.KeyboardButton('Отработка заданий')
        markup.add(z, slo, soch, ot)
        bot.send_message(message.chat.id, "Теория к каждому заданию, словари, сочинение, отработка заданий",
                         reply_markup=markup)

    elif message.text == 'Словари':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        sl = types.KeyboardButton('Орфографический')
        par = types.KeyboardButton('Паронимы')
        markup.add(sl, par)
        bot.send_message(message.chat.id, "Орфографический или паронимы",
                         reply_markup=markup)
    elif message.text == 'Орфографический':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        ab = types.KeyboardButton('А-Б')
        vi = types.KeyboardButton('В-И')
        ko = types.KeyboardButton('К-О')
        ps = types.KeyboardButton('П-С')
        tu = types.KeyboardButton('Т-Ю')
        markup.add(ab,vi, ko, ps, tu)
        bot.send_message(message.chat.id, 'Выбери на какие буквы', reply_markup=markup)
    elif message.text == 'А-Б':
        abb=open('Desktop - 1а-б.jpg', 'rb')
        bot.send_photo(message.chat.id, abb)
        orfo(message)
    elif message.text == 'В-И':
        vii=open('Desktop - 1в-и.jpg', 'rb')
        bot.send_photo(message.chat.id, vii)
        orfo(message)
    elif message.text == 'К-О':
        koo=open('Desktop - 1к-о.jpg', 'rb')
        bot.send_photo(message.chat.id, koo)
        orfo(message)
    elif message.text == 'П-С':
        pss=open('Desktop - 1п-с.jpg', 'rb')
        bot.send_photo(message.chat.id, pss)
        orfo(message)
    elif message.text == 'Т-Ю':
        tuu=open('Frame 1т-ю.jpg', 'rb')
        bot.send_photo(message.chat.id, tuu)
        orfo(message)
    elif message.text == 'Паронимы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=6)
        av = types.KeyboardButton('А-В')
        gj = types.KeyboardButton('Г-Ж')
        zl = types.KeyboardButton('З-Л')
        mo = types.KeyboardButton('М-О')
        pr = types.KeyboardButton('П-Р')
        si = types.KeyboardButton('С-Я')
        markup.add(av, gj, zl,mo, pr, si )
        bot.send_message(message.chat.id, 'На какие буквы', reply_markup=markup)
    elif message.text == 'А-В':
        avv=open('Desktop - 1а-в.jpg', 'rb')
        bot.send_photo(message.chat.id, avv)
        paronim(message)
    elif message.text == 'Г-Ж':
        gg=open('Desktop - 1г-ж.jpg', 'rb')
        bot.send_photo(message.chat.id, gg)
        paronim(message)
    elif message.text == 'З-Л':
        zz=open('Desktop - 1з-л.jpg', 'rb')
        bot.send_photo(message.chat.id, zz)
        paronim(message)
    elif message.text == 'М-О':
        mm=open('Desktop - 1м-о.jpg', 'rb')
        bot.send_photo(message.chat.id, mm)
        paronim(message)
    elif message.text == 'П-Р':
        pp=open('Desktop - 1п-р.jpg', 'rb')
        bot.send_photo(message.chat.id, pp)
        paronim(message)
    elif message.text == 'С-Я':
        ss=open('Desktop - 1с-я.jpg', 'rb')
        bot.send_photo(message.chat.id, ss)
        paronim(message)
    elif message.text == 'Сочинение':
        so = open('Desktop - 11-3.jpg', 'rb')
        so2 = open('Desktop - 14-7.jpg', 'rb')
        bot.send_photo(message.chat.id, so)
        bot.send_photo(message.chat.id, so2)
        menu(message)
    elif message.text == 'Теория к каждому заданию':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        one = types.KeyboardButton('1')
        thr = types.KeyboardButton('3')
        fr = types.KeyboardButton('4')
        fv = types.KeyboardButton('5')
        sx = types.KeyboardButton('6')
        sw = types.KeyboardButton('7')
        ei = types.KeyboardButton('8')
        nn = types.KeyboardButton('9')
        tn = types.KeyboardButton('10')
        one1 = types.KeyboardButton('11')
        tw1 = types.KeyboardButton('12')
        thr1 = types.KeyboardButton('13')
        fr1 = types.KeyboardButton('14')
        fv1 = types.KeyboardButton('15')
        sx1 = types.KeyboardButton('16')
        sw1 = types.KeyboardButton('17')
        ei1 = types.KeyboardButton('18')
        nn1 = types.KeyboardButton('19')
        tn1 = types.KeyboardButton('20')
        one2 = types.KeyboardButton('21')
        sx2 = types.KeyboardButton('26')
        markup.add(one, thr, fr, fv, sx, sw, ei, nn, tn, one1, tw1, thr1, fr1, fv1, sx1, sw1, ei1, nn1, tn1, one2, sx2)
        bot.send_message(message.chat.id, 'Выбери задание', reply_markup=markup)
    elif message.text == '1':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Frame 11.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 11.1.jpg', 'rb')), ])
        bot.send_message(message.chat.id, 'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=354')
        teor(message)

    elif message.text == '3':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Desktop - 13.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Frame 13.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Frame 23.3.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Frame 33.4.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Frame 43.5.jpg', 'rb')), ])
        bot.send_message(message.chat.id, 'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=356')
        teor(message)
    elif message.text == '4':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Desktop - 14.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 24.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 34.3.jpg', 'rb')),])
        bot.send_message(message.chat.id, 'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=340')
        teor(message)
    elif message.text == "5":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Отработка задания",
                                              url="https://rus-ege.sdamgia.ru/"))
        bot.send_message(message.chat.id, "Отработкаа задания", reply_markup=markup)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        par = types.KeyboardButton('Паронимы')
        st = types.KeyboardButton('Структура')
        ex = types.KeyboardButton('Теория')
        z = types.KeyboardButton('Теория к каждому заданию')
        markup.add(st, ex, z, par)
        bot.send_message(message.chat.id, "Паронимы словарь" , reply_markup=markup)

    elif message.text == '6':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Desktop - 16.1.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 26.2.jpg', 'rb')), ])
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=353')
        teor(message)
    elif message.text == '7':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Desktop - 17.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 27.2.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 47.3.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 57.4.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 67.5.png', 'rb')), ])
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=287')
        teor(message)
    elif message.text == '8':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Desktop - 18.1.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 28.2.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 38.3.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 48.4.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 58.5.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 68.6.jpg', 'rb')),])
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=333')
        teor(message)
    elif message.text == '9':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Desktop - 29.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 39.2.jpg', 'rb')), ])
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=358')
        teor(message)
    elif message.text == '10':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Desktop - 110.1.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 210.2.png', 'rb')), ])
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=348')
        teor(message)
    elif message.text == '11':
        abb = open('Desktop - 111.jpg', 'rb')
        bot.send_photo(message.chat.id, abb)
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=351')
        teor(message)
    elif message.text == '12':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Desktop - 112.1.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 212.2.png', 'rb')), ])
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=350')
        teor(message)
    elif message.text == '13':
        abb = open('Desktop - 113.png', 'rb')
        bot.send_photo(message.chat.id, abb)
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=272')
        teor(message)
    elif message.text == '14':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Desktop - 114.1.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 214.2.png', 'rb')), ])
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=273')
        teor(message)
    elif message.text == '15':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Desktop - 115.1.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 215.2.png', 'rb')), ])
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=267')
        teor(message)
    elif message.text == '16':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Desktop - 116.1.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 216.2.png', 'rb')), ])
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=277')
        teor(message)
    elif message.text == '17':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Desktop - 117.3.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 217.2.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 317.3.png', 'rb')),])
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=275')
        teor(message)
    elif message.text == '18':
        abb = open('Desktop - 118.png', 'rb')
        bot.send_photo(message.chat.id, abb)
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=306')
        teor(message)
    elif message.text == '19':
        abb = open('Desktop - 119.png', 'rb')
        bot.send_photo(message.chat.id, abb)
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=309')
        teor(message)
    elif message.text == '20':
        abb = open('Desktop - 120.png', 'rb')
        bot.send_photo(message.chat.id, abb)
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=280')
        teor(message)
    elif message.text == '21':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Desktop - 121.1.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 221.2.png', 'rb')),])
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=364')
        teor(message)

    elif message.text == '26':
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('Desktop - 126.1.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 226.2.png', 'rb')),
                                               telebot.types.InputMediaPhoto(open('Desktop - 326.3.png', 'rb')),])
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=275')
        teor(message)
    elif message.text == 'Отработка заданий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        one = types.KeyboardButton('1о')
        tw = types.KeyboardButton('2о')
        thr = types.KeyboardButton('3о')
        fr = types.KeyboardButton('4о')
        fv = types.KeyboardButton('5о')
        sx = types.KeyboardButton('6о')
        sw = types.KeyboardButton('7о')
        ei = types.KeyboardButton('8о')
        nn = types.KeyboardButton('9о')
        tn = types.KeyboardButton('10о')
        one1 = types.KeyboardButton('11о')
        tw1 = types.KeyboardButton('12о')
        thr1 = types.KeyboardButton('13о')
        fr1 = types.KeyboardButton('14о')
        fv1 = types.KeyboardButton('15о')
        sx1 = types.KeyboardButton('16о')
        sw1 = types.KeyboardButton('17о')
        ei1 = types.KeyboardButton('18о')
        nn1 = types.KeyboardButton('19о')
        tn1 = types.KeyboardButton('20о')
        one2 = types.KeyboardButton('21о')
        ei3 = types.KeyboardButton('22о')
        nn3 = types.KeyboardButton('23о')
        tn3 = types.KeyboardButton('24о')
        one3 = types.KeyboardButton('25о')
        sx2 = types.KeyboardButton('26о')
        markup.add(one, tw, thr, fr, fv, sx, sw, ei, nn, tn, one1, tw1, thr1, fr1, fv1, sx1, sw1, ei1, nn1, tn1, one2,ei3, nn3, tn3, one3, sx2)
        bot.send_message(message.chat.id, 'Выбери задание', reply_markup=markup)
    elif message.text == '1о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=354')
        otr(message)
    elif message.text == '2о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=355')
        otr(message)
    elif message.text == '3о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=356')
        otr(message)
    elif message.text == '4о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=340')
        otr(message)
    elif message.text == '5о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/')
        otr(message)
    elif message.text == '6о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=353')
        otr(message)
    elif message.text == '7о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=287')
        otr(message)
    elif message.text == '8о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=333')
        otr(message)

    elif message.text == '9о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=358')
        otr(message)
    elif message.text == '10о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=348')
        otr(message)
    elif message.text == '11о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=351')
        otr(message)
    elif message.text == '12о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=350')
        otr(message)
    elif message.text == '13о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=272')
        otr(message)
    elif message.text == '14о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=273')
        otr(message)
    elif message.text == '15о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=267')
        otr(message)
    elif message.text == '16о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=277')
        otr(message)
    elif message.text == '17о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=275')
        otr(message)
    elif message.text == '18о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=306')
        otr(message)
    elif message.text == '19о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=309')
        otr(message)
    elif message.text == '20о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=280')
        otr(message)

    elif message.text == '21о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=364')
        otr(message)

    elif message.text == '22о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=361')
        otr(message)
    elif message.text == '23о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=283')
        otr(message)
    elif message.text == '24о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=284')
        otr(message)
    elif message.text == '25о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=253')
        otr(message)
    elif message.text == '26о':
        bot.send_message(message.chat.id,
                         'Если  хочешь отработать это задание, переходи по ссылке: https://rus-ege.sdamgia.ru/test?theme=239')
        otr(message)


def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    st = types.KeyboardButton('Структура')
    ex = types.KeyboardButton('Теория')
    markup.add(st, ex)
    bot.send_message(message.chat.id, "Что дальше:структура или теория?",
                     reply_markup=markup)


def paronim(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    st = types.KeyboardButton('Структура')
    ex = types.KeyboardButton('Теория')
    par = types.KeyboardButton('Паронимы')
    markup.add(st, ex, par)
    bot.send_message(message.chat.id, "Что дальше:структура или теория?",
                     reply_markup=markup)


def orfo(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    st = types.KeyboardButton('Структура')
    ex = types.KeyboardButton('Теория')
    sl = types.KeyboardButton('Орфографический')
    markup.add(st, ex, sl)
    bot.send_message(message.chat.id, "Что дальше:структура или теория?",
                     reply_markup=markup)


def teor(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    st = types.KeyboardButton('Структура')
    ex = types.KeyboardButton('Теория')
    z = types.KeyboardButton('Теория к каждому заданию')
    markup.add(st, ex, z)
    bot.send_message(message.chat.id, "Что дальше:структура, теория или теория к каждому заданию?",
                     reply_markup=markup)

def otr(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    st = types.KeyboardButton('Структура')
    ex = types.KeyboardButton('Теория')
    ot = types.KeyboardButton('Отработкаа заданий')
    markup.add(st, ex, ot)
    bot.send_message(message.chat.id, "Что дальше:структура, теория или отработка заданий?",
                     reply_markup=markup)


bot.infinity_polling()
