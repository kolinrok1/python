number_=str (input('Введите число: '))
x=len(number_)
y=0
for i in range(x):
    True_=number_[i].isdigit()
    if True_==True:
        y=int(number_[i])+y
print(y)
