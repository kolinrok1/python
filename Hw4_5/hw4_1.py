1 Вычислить число π c заданной точностью d

pi_cel = str( input ('Введите точность числа PI: '))
pi_cel = pi_cel.count('0')
int_per = 1
sum = 0
for i in range (1000000):
    if i % 2 == 0:
        sum+= 4 / int_per
    else:
        sum-= 4 / int_per
    int_per += 2
sum = round(sum, pi_cel)
print(sum)

2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

in_num = int (input ('Введите число: '))
i=2
while in_num != 1:
    if in_num % i == 0:
        print(i, end=' ')
        in_num/=i
    else:
        i+=1
    
3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst_ = [1, 1, 2, 4, 5, 6, 6, 6, 7, 7, 8, 9, 1,9]
lst_result = []
for items in lst_:
    if lst_.count(items)<=1:
        lst_result.append(items)
print(lst_result)


4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

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
