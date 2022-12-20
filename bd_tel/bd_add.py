def bd_add():
    bd_inf =''
    bd_inf += (input('Введите имя: '))+';'
    bd_inf += (input('Введите Фамилию: '))+';'
    bd_inf += (input('Введите номер телефона: '))+';'
    bd_inf += (input('Введите описание или укажите что его нет: '))+'\n'
    with open('bd_tel.txt', 'a', encoding='UTF-8') as file:
        file.writelines(bd_inf)
    print('------------')
    print('Файл успешно добавлен')
    print('------------')
