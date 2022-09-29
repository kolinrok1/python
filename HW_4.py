from errno import ESTALE
print ('Введите логические значания 1 или 0')
x=int(input('Введите x1: '))
y=int(input('Введите y1: '))
z=int(input('Введите z1: '))
x_=int(input('Введите x2: '))
y_=int(input('Введите y2: '))
z_=int(input('Введите z2: '))
print (f'-({x} \/ {y} \/ {z}) = -{x_} /\ -{y_} /\ -{z_}' )
if x+y+z==3:
    x_true= False
else:
    x_true=True
if x_+y_+z_ == 3:
    y_true= False
else:
    y_true=True
if x_true == y_true:
    print('утверждение истино')
else:
    print('утверждение ложь')
