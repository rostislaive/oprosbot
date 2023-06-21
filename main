if __name__ == '__main__':
    pass
import telebot
from telebot import types
import opros
regis = 0
code = ['1pcggood', '2mvqgood', '3KNrgood', '4owugood', '5GBbgood', '6JSFgood', '7mpIgood', '8qhBgood', '9WLpgood', '10wUPgood']
bot = telebot.TeleBot("6123167214:AAGZjNbrcsDLWHOA5xCXdhx5zm-IzvPmTQI")
name = ''
age = 0
clas = ''
progran = ''
three_d = ''
reason = ''
namet = False
clast = False
progt = False
three_dt = False
reasont= False
why = ''
whyt = False
@bot.message_handler(commands=['start'])
def start(message):
    global regis
    a = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,f"Привет!\nЯ бот отряда InLab.\nСейчас я проведу тест для зачисления в инженерный отряд.\nЭтот тест покажет нужно ли тебе этот отряд",reply_markup=a)
    if len(code) == 0:
        bot.send_message(message.chat.id,"Регистрация окончена")
        regis = 1
    else:
        bot.send_message(message.chat.id,"Введите свой возрас.\nВ ответе должна быть только цифра, например: 13",reply_markup=None)
def can(this):
    match (this):
        case ("Да"):
            return this
        case ("Нет, но хочу научиться"):
            return this
        case ("Нет, и не хочу учиться"):
            return this
def yes(d: str):
    mark = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='да',callback_data=d)
    item2 = types.InlineKeyboardButton(text='нет',callback_data='hh')
    mark.add(item2,item1)
    return mark
@bot.message_handler(content_types=['text'])
def ansvers(message):
    global age,name,clas,progran,three_d,reason,namet,clast,progt,three_dt,reasont,whyt,why
    if namet is True:
        name = str(message.text)
        bot.send_message(message.chat.id, "Принять?", reply_markup=yes('clas'))
        namet = False
    elif clast is True:
        clas = str(message.text)
        bot.send_message(message.chat.id, "Принять?", reply_markup=yes('prog'))
        clast = False
    elif progt is True:
        progran = str(message.text)
        bot.send_message(message.chat.id, "Принять?", reply_markup=yes('three_d'))
        progt = False
    elif three_dt is True:
        three_d = str(message.text)
        bot.send_message(message.chat.id, "Принять?", reply_markup=yes('why'))
        three_dt = False
    elif whyt is True:
        why = str(message.text)
        bot.send_message(message.chat.id, "Принять?", reply_markup=yes('reason'))
        whyt = False
    elif reasont is True:
        reason = str(message.text)
        bot.send_message(message.chat.id, "Принять?", reply_markup=yes('ends'))
        reasont = False
    else:
        try:
            age = int(message.text)
            bot.send_message(message.chat.id,"Принять?", reply_markup=yes('name'))
        except(Exception):
            bot.send_message(message.chat.id, "Это, что? ")
def marki():
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton("Да")
    item2 = types.KeyboardButton("Нет, но хочу научиться")
    item3 = types.KeyboardButton("Нет, и не хочу учиться")
    markup.add(item1,item2,item3,row_width=3)
    return markup
@bot.callback_query_handler(func=lambda call: True)
def qestion(call):
    global age, name, clas, progran, three_d, reason, namet,clast,progt,three_dt,reasont,code,whyt,why
    if call.message:
        if call.data == 'name':
          namet = True
          bot.send_message(call.message.chat.id, 'Введите своё имя.')
        if call.data == 'clas':
            clast = True
            bot.send_message(call.message.chat.id, 'Введите свой класс.',)
        if call.data == 'prog':
            progt = True
            bot.send_message(call.message.chat.id,"Ты умеешь программировать?",reply_markup=marki())
        if call.data == 'three_d':
            three_dt = True
            bot.send_message(call.message.chat.id,"Ты умеешь создавть 3D модели?",reply_markup=marki() )
        if call.data == 'why':
            mark = types.ReplyKeyboardMarkup()
            ite1 = types.KeyboardButton("Беспелотники.")
            ite2 = types.KeyboardButton("Умная гидропоника.")
            ite3 = types.KeyboardButton("Робототехника.")
            ite4 = types.KeyboardButton("3d моделирование.")
            ite5 = types.KeyboardButton("Микроконтроллеры.")
            ite6 = types.KeyboardButton("Нейросети")
            ite7 =types.KeyboardButton("Всё!!!")
            mark.add(ite1, ite2, ite3, ite4, ite5,ite6,ite7, row_width=3)
            bot.send_message(call.message.chat.id, "Что тебе нравится?", reply_markup=mark)
            whyt = True

        if call.data == 'reason':
            reasont = True
            mark2 = types.ReplyKeyboardMarkup()
            ite1 = types.KeyboardButton("Мама заставила.")
            ite2 = types.KeyboardButton("Хочу научиться чему-то новому.")
            ite3 = types.KeyboardButton("Хочу скоротать время.")
            ite4 = types.KeyboardButton("Хочу найти интересных друзей.")
            ite5 = types.KeyboardButton("Люблю ковыряться в железках.")
            mark2.add(ite1,ite2,ite3,ite4,ite5,row_width=2)
            bot.send_message(call.message.chat.id,"Зачем ты идёшь в лагерь?",reply_markup=mark2)

        elif call.data == 'ends':
            if opros.test(age,progran,three_d,reason) == True:
                a = types.ReplyKeyboardRemove()
                bot.send_message(call.message.chat.id,f"{name} из {clas},ты прошёл тест!\nТвой код доступа:{code[0]}.\nТебе нравится {why}\nЭто сообщение надо отправить вожатому.\nСыллка на наш канал в телеграме -\nhttps://t.me/+pJlWOzZvaUU1ZWYy",reply_markup=a)
                code = code[1:]
                print(code)
            else: 
                bot.send_message(call.message.chat.id,"Ты не прошёл тест.")
bot.polling(none_stop=True)
