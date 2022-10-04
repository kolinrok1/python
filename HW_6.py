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


number_=int (input('Введите число: '))
x=[]
for i in range(number_):
    x.append(i+1)
result=0
for i in range(number_):
    result_n= (1 + 1 / x[i])**x[i]
    result=round(result+result_n,3)
print(result)


number_=int (input('Введите число: '))
x=[]
for i in range(number_*-1,number_+1):
    x.append(i)
print(x)
a=int (input('Введите число a: '))
b=int (input('Введите число b: '))
print (x[a-1]*x[b-1])


import random
first_arr=['345','rrrr','yyy','3432','pppp','4444']
print(first_arr)
random_arr_index=[]
count_=0
while count_!=len(first_arr):
    for i in range(len(first_arr)):
        randon_number= random.randrange(0, len(first_arr))
        if randon_number not in random_arr_index:
            random_arr_index.append(randon_number)
            count_=count_+1
second_array=[]
for i in range(len(first_arr)):
    second_array.append(first_arr[random_arr_index[i]])
first_arr=second_array
print(first_arr)
