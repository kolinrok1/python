import sqlite3
global db
global sql
db = sqlite3.connect('school.db')
sql = db.cursor()

def student_print(studen = 'Саша'):
    for value in sql.execute(f"SELECT student, lesson, home_work FROM homew WHERE student = '{studen}' "):
        print(value)
