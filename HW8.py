first_arr=[3,7,5,9,1,3]
print(first_arr)
result_: int = 0
for i in range(1,len(first_arr)):
    if i % 2 != 0:
        result_+=first_arr[i]
print(result_)

_____________________________________________________________________________

first_arr=[3,7,5,9,3]
print(first_arr)
if len(first_arr) % 2 != 0:
    long_count=len(first_arr)//2+1
else:
    long_count=len(first_arr)//2
for i in range(long_count):
    x=(len(first_arr)-i)-1
    print(first_arr[i] * first_arr[x])

 ___________________________________________________________________________   
    
first_arr=[1.1, 1.2, 3.1, 5, 10.01]
print(first_arr)
for i in range(len(first_arr)):
    x=int (first_arr[i])
    first_arr[i]=round(first_arr[i]-x,2)
print(first_arr)
max=first_arr[i]
min=first_arr[i]
for i in range (len(first_arr)):
    if first_arr[i]== 0:
        continue
    elif first_arr[i]>max:
        max=first_arr[i]
    elif first_arr[i]<min:
        min=first_arr[i]
print(max-min)

___________________________________________________________________________   
    

def cel_to_(num):
    cel=""
    while num!=0:
        cel=str(num % 2) +str(cel)
        num=num//2
    return(cel)

x=int(input('Введите число: '))
print(cel_to_(x))

___________________________________________________________________________   
    
 x=int(input('Введите число: '))
result_=0
result_second=1
count_=0
list_=[0]
while count_<x:
    result_x=result_
    result_=result_+result_second
    result_second=result_x
    count_+=1
    list_.append(result_)
    list_.insert(0,result_*-1)
print(list_)
