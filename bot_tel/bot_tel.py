from telebot import TeleBot, types

TOKEN = '5732115238:AAGxqCFfykuLyuyV65BoJpwxvxhay-Cei-8'

bot = TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'help'])
def but_menu(msg: types.Message):
    bot.send_message(msg.chat.id, 'Доступные действия:' + '\n' + '/print_all' + '\n' + '/add_record'
                     + '\n' + '/import' + '\n' + '/export')


@bot.message_handler(commands=['print_all'])
def but_menu(msg: types.Message):
    line_print = ''
    flag = True
    with open('bd_tel.txt', 'r', encoding='UTF-8') as file:
        while flag != False:
            inf_bd = file.readline()
            if not inf_bd:
                flag = False
                continue
            inf_split = inf_bd.split(';')
            line_print = 'Фамилия: ' + inf_split[0] + '\n' + 'Имя: ' + inf_split[1] + '\n' + 'Номер телефона: ' + \
                         inf_split[2] + '\n' + \
                         'Описание: ' + inf_split[3]
            bot.send_message(msg.chat.id, line_print)


@bot.message_handler(commands=['add_record'])
def but_menu(msg: types.Message):
    if msg.text != 'add_record':
        bot.send_message(msg.chat.id, 'Введите фамилию')
        bd_inf = ''
        #bot.send_message(msg.chat.id, 'Введите фамилию')
        bd_inf += msg.text + ';'
        bot.send_message(msg.chat.id, 'Введите имя')
        bd_inf += msg.text + ';'
        bot.send_message(msg.chat.id, 'Введите номер телефона')
        bd_inf += msg.text + ';'
        bot.send_message(msg.chat.id, 'Введите описание')
        bd_inf += msg.text + ';'
        bot.send_message(msg.chat.id, bd_inf)

bot.polling(none_stop=True, interval=0)
