1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def sum(num_sum):
    result = 0
    for i in range (len (num_sum)):
        if num_sum[i].isdigit():
            result += int(num_sum[i])
    return result

num = str (input('Введите число: '))
print(sum (num))

Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def fact(num_fact):
    result = 1
    for i in range (1, num_fact + 1):
        result *= i
    return result

in_num = int (input ('Введите число: '))
count_=1
while count_ != in_num + 1:
    print(fact (count_), end=' ')
    count_ += 1

   Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму
  
def lst_num(num):
    lst = []
    result = 0
    for i in range (1, num + 1):
        lst.append((1 + 1 / i)**i)
        result += lst[i - 1]
    print(lst)
    return result

in_num = int( input ('Введите число: '))
print((lst_num(in_num)))

Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

in_num = int (input ('Введите число: '))
lst=[]
for i in range (in_num * -1, in_num + 1):
    lst.append(i)
print(lst)
ferst_num = int (input('Введите номер первого элемента: '))
second_num = int (input('Введите номер второго элемнта: '))
print (f'Сумма {ferst_num} элемента и {second_num} элеменнта, ровна {lst[ferst_num] + lst[second_num]}')

 Реализуйте алгоритм перемешивания списка.
  
  from random import randint

ferst_lst=[1, 2,3 , 4, 5, 6, 7, 8, 9, 10]
print(ferst_lst)
index_list=[]
count_=len(ferst_lst)
while count_ != 0:
    index_ = randint(0,len(ferst_lst)-1)
    if index_ not in index_list:
        index_list.append(index_)
        count_-=1
new_lst=[]
for i in range(len(index_list)):
    new_lst.append(ferst_lst[index_list[i]])
ferst_lst = new_lst
print(ferst_lst)
