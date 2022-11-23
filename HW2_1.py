dey_= int (input ('Введите число от 1 до 7: '))
if dey_ < 1 or dey_ > 7:
    print('Введите корректное число')
elif dey_ == 6 or dey_ == 7:
    print('Выходной')
else:
    print('Рабочий день')
 ________________________________________
for x in range(2):
    for y in range(2):
        for z in range(2):
            for x2 in range(2):
                for y2 in range(2):
                    for z2 in range(2):
                        if (x + y + z == 0 and x2 + y2 + z2 == 0) or (x + y + z == 3 and x2 + y2 + z2 == 3):
                            print(f'-({x}\/{y}\/{z}) = -{x2}/\-{y2}/\-{z2} - true')
                        else:
                            print(f'-({x}\/{y}\/{z}) = -{x2}/\-{y2}/\-{z2} - folse')
 ______________________________________________________________
x=int (input('введите координату Х: '))
y=int (input('введите координату Y: '))
if x == 0 or y == 0 :
    print('Введите корректные значения')
    exit
if x > 0 and y > 0:
    print('первая четверть')
elif x > 0 and y < 0:
    print ('Вторая четветь')
elif x < 0 and y < 0:
    print ('Третья четветь')
elif x < 0 and y > 0:
    print ('Четвертая четветь')
_______________________________________________________________
x=int (input('введите номер четверти: '))
if x == 1:
    print('Х>0 \nY>0')
elif x==2:
    print ('Х>0 \nY<0')
elif x == 3:
    print ('Х<0 \nY<0')
elif x == 4:
    print ('Х<0 \nY>0')
 __________________________________________________________________
print('Введите координаты двух точек')
x1=float(input('Введите х1: '))
y1=float(input('Введите y1: '))
x2=float(input('Введите х2: '))
y2=float(input('Введите y2: '))
result_ = round(((x2-x1)**2+(y2-y1)**2)**0.5,3)
print(result_)
