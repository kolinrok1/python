def import_bd():
    name_bd = input('Введите название импортируемого файла:')
    print('Выберите формат импортируемого файла:\n 1.- Фамилия_1;Имя_1;Телефон_1;Описание_1;'
          'Фамилия_2;Имя_2;Телефон_2;Описание_2;\n 2.- Фамилия_1;Имя_1;Телефон_1;Описание_1;'
          '\nФамилия_2;Имя_2;Телефон_2;Описание_2;')
    type_bd = input('Введите формат импортируемого файла:')
    return name_bd, type_bd

def import_bd_1(name_bd):
    with open(name_bd, 'r', encoding='UTF-8') as file:
        imp_bd = file.readline()
    bd = imp_bd.split(';')
    str_items = ''
    count_ = 0
    for items, value in enumerate(bd):
        if count_ == 4:
            str_items += '\n'
            count_ = 0
        count_ += 1
        if items != len(bd)-1:
            str_items += value+';';
    with open('bd_tel.txt', 'a', encoding='UTF-8') as file:
        file.writelines(str_items)
    print('------------')
    print('Файл успешно импортирован')
    print('------------')


def import_bd_2 (name_bd):
    with open(name_bd, 'r', encoding='UTF-8') as file:
        imp_bd = file.readline()
    with open('bd_tel.txt', 'a', encoding='UTF-8') as file:
        file.writelines(imp_bd)
    print('------------')
    print('Файл успешно импортирован')
    print('------------')
