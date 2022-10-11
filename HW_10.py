Задача 2:
x=int(input('Введите число: '))
count_=1
while x!=1:
    count_+=1
    if x%count_==0:
        x=x/count_
        print(count_, end=' ')
        count_=1
        
 Задача 3:
  from itertools import count


first_arr=[1,1,2,3,3,4,1,5,7,8,8,7,9]
count_=0
first_list=[]
for i in range(len(first_arr)):
    count_=first_arr.count(first_arr[i])
    if count_==1 :
        first_list.append(first_arr[i])
print(first_list)

Задача 4:
 import random
x=int(input('Введите число: '))
list_mul_num=[]
for i in range (1,100):
    if random.randrange(1,3)==1:
        list_mul_num.append(f'{random.randrange(1,100)}*x^{x} - {random.randrange(1,100)}^{x} = 0 ')
    if random.randrange(1,3)==2:
        j= random.randrange(1,10)
        list_mul_num.append(f'{random.randrange(1,100)}^{x} -{random.randrange(1,100)} = 0 ')
    if  random.randrange(1,3)==3:
        j= random.randrange(1,10)
        list_mul_num.append(f'{random.randrange(1,100)}^{x} = 0 ')
data_= open ('multy_num','w')
data_.write(str(list_mul_num))
data_.close

