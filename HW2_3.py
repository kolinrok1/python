Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
lst_=[2, 3, 5, 9, 3]
result = lst_[0]
for i in range (1, len(lst_), 2):
    result += lst_[i]
print(result)

Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
lst_ = [2, 3, 4, 5, 6, 8]
lst_result = []
index_len = 0
if len(lst_) % 2 != 0 :
    index_len = 1
for i in range(len(lst_)//2 + index_len):
    lst_result.append(lst_[i] * lst_[0-(i+1)])
print(lst_result)

Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def num_int (num):
    return round (num - int(num),3)
    
lst_ = [1.1, 1.2, 3.1, 5, 10.01]
max_ = float('-inf')
min_ = float('inf')
for index in lst_:
    if num_int(index) != 0:
        if max_ < (num_int(index)):
          max_ =  (num_int(index))
        if min_ > (num_int(index)):
             min_ = (num_int(index))
print(max_ - min_)

Втрой вариант решения:
  
def num_int (num):
    return round (num - int(num),3)
    
lst_ = [1.1, 1.2, 3.1, 5, 10.01]
lst_fract = []
for index in lst_:
    if num_int(index) != 0:
        lst_fract.append(num_int(index))
max_ = lst_fract[0]
min_ = lst_fract[0]
for i in range(len(lst_fract)):
    if max_ < lst_fract[i]:
        max_ = lst_fract[i]
    if min_ > lst_fract[i]:
        min_ = lst_fract[i]
print (lst_fract)
print(max_ - min_)

Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def cel_to_(num):
    cel=""
    while num!=0:
        cel=str(num % 2) +str(cel)
        num=num//2
    return(cel)

x=int(input('Введите число: '))
print(cel_to_(x))

Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
in_num = int (input('Введите число'))
lst_=[0]
for count_ in range(1,in_num+1):
    if count_ == 1:
        lst_.append(1)
    else:
        lst_.append(lst_[count_-2] - lst_[count_-1])
lst_.reverse()
for count_ in range(len(lst_),in_num+len(lst_)):
    if count_ == len(lst_)-1:
        lst_.append(1)
    else:
        lst_.append(lst_[count_-1] + lst_[count_-2])
print(lst_)
