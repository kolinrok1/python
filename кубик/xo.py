import emoji

def tabl (step_player, x, str_):
    
    str_[step_player - 1] = x
    print(f'{str_[0]}|{str_[1]}|{str_[2]} \n-----\n{str_[3]}|{str_[4]}|{str_[5]}\n-----\n{str_[6]}|{str_[7]}|{str_[8]} ')
    return str_

def check_win (str_, x):
    pl = 'перый игрок'
    if x == emoji.emojize(':red_circle:'):
        pl = 'второй игрок'
    if (str_[0] == x and str_[1] == x and str_[2] == x) or (str_[0] == x and str_[3] == x and str_[6] == x):
        print ('Выйграл ' + pl)
        exit()
    if (str_[3] == x and str_[4] == x and str_[5] == x) or ((str_[1] == x and str_[4] == x and str_[7] == x)):
        print ('Выйграл ' + pl)
        exit()
    if (str_[6] == x and str_[7] == x and str_[8] == x) or ((str_[2] == x and str_[5] == x and str_[8] == x)):
        print ('Выйграл ' + pl)
        exit()
    if (str_[0] == x and str_[4] == x and str_[8] == x) or ((str_[2] == x and str_[4] == x and str_[6] == x)):
        print ('Выйграл ' + pl)
        exit()

str_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fin = 0
player = 1
print('1|2|3 \n-----\n4|5|6\n-----\n7|8|9 ')
while fin != 8:
    fin+=1
    if player % 2 != 0:
        player = int(input('Первый игрок куда сходим?: '))
        tabl(player, emoji.emojize(':white_circle:'), str_)
        player = 2
        check_win(str_, emoji.emojize(':white_circle:'))
    elif player % 2 == 0:
        player = int(input('Второй игрок куда сходим?: '))
        tabl(player, emoji.emojize(':red_circle:'), str_)
        player = 1
        check_win(str_, emoji.emojize(':red_circle:'))
print('Ничья')
