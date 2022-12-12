from random import randint
candy = 2021
max_step = 28

def man ():
    while True:
        step_man = int(input(f'Осталось {candy} конфет. Сколько возьмешь?\n Беру:  '))
        if 1 <= step_man <= min(max_step,candy):
            return int(step_man)

def bot():
    step_bot = randint (1, min(candy, max_step))
    print(f'Бот взял {step_bot} конфет')
    return step_bot


print('Кто взял последнюю конфету тот и победил.\n Кто первый ходит определит случай!')
man_ = randint (0, 1)
if man_ == 0:
    man_ = True
    print('Первый ходит человек')
else:
    man_ = False
    print('Первый ходит бот')
print(f'На столе {candy} конфет')
flag = True
while flag == True:
    if man_:
        candy -= man()
        if candy == 0:
           print ('Победил человек')
           flag = False
    else:
        candy-= bot()
        if candy == 0:
           print ('Победил бот')
           flag = False
    man_ = not man_
