def print_bd():
    flag = True
    with open('bd_tel.txt', 'r', encoding='UTF-8') as file:
        while flag != False:
            inf_bd = file.readline()
            if not inf_bd:
                flag = False
                continue
            inf_split = inf_bd.split(';')
            print('Фамилия: ' + inf_split[0])
            print('Имя: ' + inf_split[1])
            print('Номер телефона: ' + inf_split[2])
            print('Описание: ' + inf_split[3])
            print('-----------')
