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
        bot.send_message(msg.chat.id, 'Введите выражение через  пробел')

    elif msg.text == 'комплексные числа':
        bot.send_message(msg.chat.id, 'Введите два числа через  пробел')
        bot.register_next_step_handler(msg, complex_)

@bot.message_handler()
def rac_num(msg: types.Message):
    log_(msg)
    text = msg.text.split(' ')
    if text[1] == '+':
        bot.send_message(msg.chat.id, text=f'Результат сложения {float(text[0]) + float(text[2])}')
    elif text[1] == '-':
        bot.send_message(msg.chat.id, text=f'Результат сложения {float(text[0]) - float(text[2])}')
    elif text[1] == '*':
        bot.send_message(msg.chat.id, text=f'Результат сложения {float(text[0]) * float(text[2])}')
    elif text[1] == '/':
        if text[2] != '0':
            bot.send_message(msg.chat.id, text=f'Результат сложения {float(text[0]) * float(text[2])}')
        else:
            bot.send_message(msg.chat.id, text=f'На 0 делить нельзя')

@bot.message_handler()
def complex_(msg: types.Message):
    log_(msg)
    text = msg.text.split(' ')
    if text[1] == '+':
        a,b= num_cal_1(msg)
        x, y = num_cal_2(msg)
        bot.send_message(msg.chat.id, text=f'Результат сложения {a+x}"+"{y+b}')
    elif text[1] == '-':
        a,b= num_cal_1(msg)
        x, y = num_cal_2(msg)
        bot.send_message(msg.chat.id, text=f'Результат сложения {a-x}"+"{y-b}')
    elif text[1] == '*':
        a,b= num_cal_1(msg)
        x, y = num_cal_2(msg)
        bot.send_message(msg.chat.id, text=f'Результат сложения {a*x}"+"{y*b}')
    elif text[1] == '/':
        a,b= num_cal_1(msg)
        x, y = num_cal_2(msg)
        bot.send_message(msg.chat.id, text=f'Результат сложения {a/x}"-"{y/b}')

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
        return (float(num[0]), float(num[1][:-1]) * -1)
    elif x_ == '+':
        return (float(num[0]), float(num[1][:-1]))

def num_cal_2(msg: types.Message):
    a = msg.text.split(' ')
    num_2 = a[2]
    x_ = ''
    for i in range(len(num_2)):
        if str(num_2[i]) == '+':
            x_ = num_2[i]
        if x_ == '':
            x_ = '-'
    num = num_2.split(x_)
    if x_ == '-':
        return (float(num[0]), float(num[1][:-1]) * -1)
    elif x_ == '+':
        return (float(num[0]), float(num[1][:-1]))


bot.polling(none_stop=True, interval=0)
