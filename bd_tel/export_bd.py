def export_bd ():
    name_bd = input('Введите название экспортируемого файла:')
    with open('bd_tel.txt', 'r', encoding='UTF-8') as file:
        ex_bd = file.read()
    with open(name_bd, 'a', encoding='UTF-8') as file:
        file.writelines(ex_bd)
    print('------------')
    print('Файл успешно экспортирован')
    print('------------')
