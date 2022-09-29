x=int (input('введите координату Х: '))
y=int (input('введите координату Y: '))
if x==0 or y== 0 :
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
