number_=str (input('Введите число: '))
x=len(number_)
y=0
for i in range(x):
    True_=number_[i].isdigit()
    if True_==True:
        y=int(number_[i])+y
print(y)


number_=int (input('Введите число: '))
x=[]
for i in range(number_):
    x.append(i+1)
y=0
while number_!=y:
    result=1
    for i in range(y):
        result=x[i+1]* result
    print(result)
    y=y+1
print()
