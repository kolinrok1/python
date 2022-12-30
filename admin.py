import sqlite3
global db
global sql
db = sqlite3.connect('school.db')
sql = db.cursor()

'''
sql.execute("""CREATE TABLE users(
    login TEXT,
    password TEXT,
    rul TEXT
)""")
db.commit()
sql.execute("""CREATE TABLE homew(
    student TEXT,
    teach TEXT,
    lesson TEXT,
    home_work TEXT
)""")
db.commit()
'''
def reg_():
    log_ = input('Введите логин: ')
    pas_ = input('Введите пароль: ')
    rul_ = input('Введите роль')

    sql.execute(f"SELECT login FROM users WHERE login = '{log_}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES ('{log_}', '{pas_}', '{rul_}')")
        db.commit()
        print('Регистрация успешна')
    else:
        print('Такой пользователь уже имеется')

def admin_print():
    for value in sql.execute("SELECT * FROM users"):
        print(value)

def admin_delet():
    log_ = input('Введите пользователя которого нужно удалить: ')
    sql.execute(f"SELECT login FROM users WHERE login = '{log_}'")
    if sql.fetchone() is not None:
        sql.execute(f"DELETE FROM users WHERE login = '{log_}'")
        db.commit()
        print('Пользователь успешно удален')
    else:
        print('Такого пользователя нет в базе')

