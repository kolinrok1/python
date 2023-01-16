from telebot import TeleBot, types
import datetime
import sqlite3
global db
global sql

db = sqlite3.connect('cacl_log.db')
sql = db.cursor()
'''sql.execute("""CREATE TABLE calc_user(
    data TEXT,
    user TEXT,
    log TEXT
    data TEXT
)""")
db.commit()'''

TOKEN = '5837915740:AAFIhs4pE28dyqD3F3Jbk0bFL12oTYwZDpY'

bot = TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def button_calc(msg: types.Message):
    mark_but = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mark_but.add(types.KeyboardButton('рациональные числа'), types.KeyboardButton('комплексные числа'))
    but_msg = bot.send_message(msg.chat.id, 'Выберите действие', reply_markup=mark_but)
    bot.register_next_step_handler(but_msg, answer)


def answer(msg: types.Message):
    if msg.text == 'рациональные числа':
        bot.register_next_step_handler(msg, rac_num)
        bot.send_message(msg.chat.id, 'Введите выражение через  пробел (например 4 + 6)')

    elif msg.text == 'комплексные числа':
        bot.send_message(msg.chat.id, 'Введите выражение через  пробел (например 4-8b + 5-9b)')
        bot.register_next_step_handler(msg, complex_)

@bot.message_handler()
def rac_num(msg: types.Message):
    log_(msg)
    text = msg.text.split(' ')
    if text[0].isdigit() and text[2].isdigit():
        if text[1] == '+':
            bot.send_message(msg.chat.id, text=f'Результат сложения {float(text[0]) + float(text[2])}')
        elif text[1] == '-':
            bot.send_message(msg.chat.id, text=f'Результат вычетания {float(text[0]) - float(text[2])}')
        elif text[1] == '*':
            bot.send_message(msg.chat.id, text=f'Результат умножения {float(text[0]) * float(text[2])}')
        elif text[1] == '/':
            if text[2] != '0':
                bot.send_message(msg.chat.id, text=f'Результат деления {float(text[0]) * float(text[2])}')
            else:
                bot.send_message(msg.chat.id, text=f'На 0 делить нельзя')
    else:
        bot.send_message(msg.chat.id, 'Введите корректное значение(рациональные числа)')

@bot.message_handler()
def complex_(msg: types.Message):
    log_(msg)
    text = msg.text.split(' ')
    if len(text) == 3:
        x, y, w = num_cal_2(msg)
        a, b, c = num_cal_1(msg)
        if text[1] == '+':
            bot.send_message(msg.chat.id, text=f'Результат сложения {a+x}+{y+b}{c}')
        elif text[1] == '-':
            bot.send_message(msg.chat.id, text=f'Результат вычетания {a-x}+{y-b}{c}')
        elif text[1] == '*':
            bot.send_message(msg.chat.id, text=f'Результат умножения {a*x}+{y*b}{c}')
        elif text[1] == '/':
            bot.send_message(msg.chat.id, text=f'Результат деления {a/x}+{y/b}{c}')
    else:
        bot.send_message(msg.chat.id, 'Введите корректное значение(комплексные числа)')

def log_(msg):
    db = sqlite3.connect('cacl_log.db')
    sql = db.cursor()
    sql.execute(f"INSERT INTO calc_user VALUES ('{datetime.date.today()}', '{msg.from_user.first_name}', '{msg.text}')")
    db.commit()
    for item in sql.execute('SELECT * FROM calc_user'):
        print(item)

@bot.message_handler()
def num_cal_1(msg: types.Message):
    a = msg.text.split(' ')
    num_1 = a[0]
    x_ = ''
    for i in range(len(num_1)):
        if str(num_1[i]) == '+':
            x_ = num_1[i]
        if x_ == '':
            x_ = '-'
    num = num_1.split(x_)
    if x_ == '-':
        return (float(num[0]), float(num[1][:-1]) * -1, num[1][-1])
    elif x_ == '+':
        return (float(num[0]), float(num[1][:-1]) * -1, num[1][-1])

@bot.message_handler()
def num_cal_2(msg: types.Message):
    a = msg.text.split(' ')
    num_1 = a[2]
    x_ = ''
    for i in range(len(num_1)):
        if str(num_1[i]) == '+':
            x_ = num_1[i]
        if x_ == '':
            x_ = '-'
    num = num_1.split(x_)
    if x_ == '-':
        return (float(num[0]), float(num[1][:-1]) * -1 , num[1][-1])
    elif x_ == '+':
        return (float(num[0]),float(num[1][:-1]) * -1, num[1][-1])


bot.polling(none_stop=True, interval=0)
