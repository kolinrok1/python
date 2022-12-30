import sqlite3
global db
global sql
db = sqlite3.connect('school.db')
sql = db.cursor()

def teach_print ():
    studen = input('Введите имя ученика для просмотра ДЗ')
    for value in sql.execute(f"SELECT student, lesson, home_work FROM homew WHERE student = '{studen}' "):
        print(value)

def teach_add_hw(teach = 'Аня'):
    studen = input('Введите имя ученика кому добавить ДЗ')
    sql.execute(f"SELECT login FROM users WHERE login = '{studen}' AND rul = 'ученик'")
    if sql.fetchone() is not None:
        less = input('Введите урок : ')
        hw = input('Введите введите домашнее')
        sql.execute(f"INSERT INTO homew VALUES ('{studen}', '{teach}', '{less}', '{hw}')")
        db.commit()
        print('Домашнее задание добавлено')
        for value in sql.execute("SELECT * FROM homew"):
            print(value)
    else:
        print('Такой пользователь не найден, обратитесь к администратору')