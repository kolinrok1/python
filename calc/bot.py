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
)""")
db.commit()'''

TOKEN = '5837915740:AAFIhs4pE28dyqD3F3Jbk0bFL12oTYwZDpY'

bot = TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def button_calc(msg: types.Message):
    mark_but = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mark_but.add(types.KeyboardButton('+'), types.KeyboardButton('-'),
                 types.KeyboardButton('*'), types.KeyboardButton('/'))
    but_msg = bot.send_message(msg.chat.id, 'Выберите действие', reply_markup=mark_but)
    bot.register_next_step_handler(but_msg, answer)

def answer(msg: types.Message):
    if msg.text == '+':
        bot.send_message(msg.chat.id, 'Введите два числа через  пробел')
        bot.register_next_step_handler(msg, sum_)
    elif msg.text == '-':
        bot.send_message(msg.chat.id, 'Введите два числа через  пробел')
        bot.register_next_step_handler(msg, subtractions)
    elif msg.text == '*':
        bot.send_message(msg.chat.id, 'Введите два числа через  пробел')
        bot.register_next_step_handler(msg, multiplication)
    elif msg.text == '/':
        bot.send_message(msg.chat.id, 'Введите два числа через  пробел')
        bot.register_next_step_handler(msg, division)


def subtractions(msg: types.Message):
    str_cal = ''
    a, b = map(float, msg.text.split())
    str_cal = str(a) + '-' + str(b)
    log_(msg, str_cal)
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a - b}')

def sum_(msg: types.Message):
    str_cal = ''
    a, b = map(float, msg.text.split())
    str_cal = str(a) + '+' + str(b)
    log_(msg, str_cal)
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')

def multiplication(msg: types.Message):
    str_cal = ''
    a, b = map(float, msg.text.split())
    str_cal = str(a) + '*' + str(b)
    log_(msg, str_cal)
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a * b}')

def division(msg: types.Message):
    str_cal = ''
    a, b = map(float, msg.text.split())
    str_cal = str(a) + '/' + str(b)
    log_(msg, str_cal)
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a / b}')

def log_(msg: types.Message, str_calc):
    db = sqlite3.connect('cacl_log.db')
    sql = db.cursor()
    sql.execute(f"INSERT INTO calc_user VALUES ('{datetime.date.today()}', '{msg.from_user.first_name}', '{str_calc}')")
    db.commit()
    #for item in sql.execute('SELECT * FROM calc_user'):
    #    print(item)

bot.polling(none_stop=True, interval=0)
