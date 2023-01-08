from telebot import TeleBot, types
import os

TOKEN = '5732115238:AAGxqCFfykuLyuyV65BoJpwxvxhay-Cei-8'

bot = TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def but_menu(msg: types.Message):
    mark_but = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mark_but.add(types.KeyboardButton('Вывести все записи'), types.KeyboardButton('Добавить новую запись'),
                 types.KeyboardButton('Импортировать'), types.KeyboardButton('Экспортировать'))
    but_msg = bot.send_message(msg.chat.id, 'Выберите действие', reply_markup=mark_but)
    bot.register_next_step_handler(but_msg, answer)



def answer(msg: types.Message):
    if msg.text == 'Вывести все записи':
        print_tel(msg)
    elif msg.text == 'Добавить новую запись':
        bot.send_message(msg.chat.id, 'Введите через пробел: Фамилию, Имя, Номер телефона, Описание')
        bot.register_next_step_handler(msg, add_tel)
    elif msg.text == 'Экспортировать':
        bot.register_next_step_handler(msg, export_)
    elif msg.text == 'Импортировать':
        bot.send_message(msg.chat.id, 'Загрузите необходимый файл')
        bot.register_next_step_handler(msg, import_)

def print_tel(msg: types.Message):
    line_print = ''
    flag = True
    with open('bd_tel.txt', 'r', encoding='UTF-8') as file:
        while flag != False:
            inf_bd = file.readline()
            if not inf_bd:
                flag = False
                continue
            inf_split = inf_bd.split(';')
            line_print = 'Фамилия: ' + inf_split[0]+'\n' + 'Имя: ' + inf_split[1]+'\n' + 'Номер телефона: ' + inf_split[2]+'\n' +\
                         'Описание: ' + inf_split[3]
            bot.send_message(msg.chat.id, line_print)
    bot.register_next_step_handler(msg, but_menu)


def add_tel(msg: types.Message):
    bot.send_message(msg.chat.id, msg.text)
    text_ = msg.text.replace(' ', ';') + '\n'
    with open('bd_tel.txt', 'a', encoding='UTF-8') as file:
        file.writelines(text_)
    bot.register_next_step_handler(msg, but_menu)


def export_(msg: types.Message):
    bot.send_document(msg.chat.id, document=open('bd_tel.txt'))
    bot.register_next_step_handler(msg, but_menu)


@bot.message_handler(content_types=['document'])
def import_(msg: types.Message):
    filename = msg.document.file_name
    with open(filename, 'wb') as file:
        file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
    with open(filename, 'r', encoding='UTF-8') as file:
        imp_bd = file.readline()
    bd = imp_bd.split(';')
    str_items = ''
    count_ = 0
    for items, value in enumerate(bd):
        if count_ == 4:
            str_items += '\n'
            count_ = 0
        count_ += 1
        if items != len(bd) - 1:
            str_items += value + ';';
    with open('bd_tel.txt', 'a', encoding='UTF-8') as file:
        file.writelines(str_items)
    os.remove(filename)
    bot.send_message(msg.chat.id, 'Данный успешно импортированны')
    bot.register_next_step_handler(msg, but_menu)


bot.polling(none_stop=True, interval=0)
