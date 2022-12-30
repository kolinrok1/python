import sqlite3
import admin
import teach
import studend
global db
global sql
db = sqlite3.connect('school.db')
sql = db.cursor()

'''
Пользователи
('root', '1', 'admin')
('Миша', '2', 'ученик')
('Саша', '2', 'ученик')
('Даша', '2', 'ученик')
('Лида', '3', 'учитель')
('Аня', '3', 'учитель')
'''

print('-----------------')
print('Войдите в систему')
print('-----------------')
flag = True
while flag != False:
    log_ = input('Введите логин: ')
    pas = input('Введите пароль: ')
    sql.execute(f"SELECT login FROM users WHERE login = '{log_}' AND password = '{pas}'")
    if sql.fetchone() is not None:
        sql.execute(f"SELECT rul FROM users WHERE login = '{log_}' AND password = '{pas}'")
        rul = sql.fetchone()[0]
        print('Вы успешно вошли в систему')
        flag = False
    else:
        print('Не верный логин или пароль')
if rul == 'admin':
    flag = True
    while flag != False:
        print('Добро пожаловать администратор')
        print('Выбериет необходимые действия:')
        print(' 1 - вывести на экран всех пользователей')
        print(' 2 - добавить нового пользователя')
        print(' 3 - удалить пользователя')
        print(' 4 - выход')
        button = input('Введите цифру:')
        if button == '1':
            admin.admin_print()
        elif button == '2':
            admin.reg_()
        elif button == '3':
            admin.admin_delet()
        elif button == '4':
            exit()
if rul == 'учитель':
    flag = True
    while flag != False:
        print('Добро пожаловать вы вошли как учитель')
        print('Выберите необходимые действия:')
        print(' 1 - вывести на экран ДЗ ученика')
        print(' 2 - добавить ДЗ ученику')
        print(' 3 - выход')
        button = input('Введите цифру:')
        if button == '1':
            teach.teach_print()
        elif button == '2':
            teach.teach_add_hw(log_)
        elif button == '3':
            exit()
if rul == 'ученик':
    flag = True
    while flag != False:
        print('Добро пожаловать вы вошли как ученик')
        print('Выберите необходимые действия:')
        print(' 1 - просмотр своего ДЗ')
        print(' 2 - выход')
        button = input('Введите цифру:')
        if button == '1':
            studend.student_print(log_)
        if button == '2':
            exit()