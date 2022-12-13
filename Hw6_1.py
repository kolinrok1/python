
Было
lst_=[2, 3, 5, 9, 3]
result = lst_[0]
for i in range (1, len(lst_), 2):
    result += lst_[i]
print(result)
Стало
lst_=[2, 3, 5, 9, 3]
result = lst_[0]
for items, value in enumerate (lst_):
    if items % 2 != 0: 
        result += value
print(result)
__________

Было 
lst_ = [2, 3, 4, 5, 6, 8]
lst_result = []
index_len = 0
if len(lst_) % 2 != 0 :
    index_len = 1
for i in range(len(lst_)//2 + index_len):
    lst_result.append(lst_[i] * lst_[0-(i+1)])
print(lst_result)
Стало
lst_ = list(map(int, input('Введите ряд чисел: ').split()))
lst_result = []
index_len = 0
if len(lst_) % 2 != 0 :
    index_len = 1
for i in range(len(lst_)//2 + index_len):
    lst_result.append(lst_[i] * lst_[0-(i+1)])
print(lst_result)
________

Было
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

Стало

def num_int (num):
    return round (num - int(num),3)
    
lst_ = list(map(int, input('Введите ряд цифр: ').split()))
max_ = float('-inf')
min_ = float('inf')
for index in lst_:
    if num_int(index) != 0:
        if max_ < (num_int(index)):
          max_ =  (num_int(index))
        if min_ > (num_int(index)):
             min_ = (num_int(index))
print(max_ - min_)
__________________

Было
lst_ = [1, 1, 2, 4, 5, 6, 6, 6, 7, 7, 8, 9, 1,9]
lst_result = []
for items in lst_:
    if lst_.count(items)<=1:
        lst_result.append(items)
print(lst_result)
Стало
lst_ = [1, 1, 2, 4, 5, 6, 6, 6, 7, 7, 8, 9, 1,9]
lst_result = []
for items, value in enumerate (lst_):
    if lst_.count(value) <= 1:
        lst_result.append(value)
print(lst_result)
