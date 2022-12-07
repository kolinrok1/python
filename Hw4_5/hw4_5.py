def str_mult (str_):
    lst_= []
    str_char=str_[0]
    return str_char.split(' ')

def opl (num_opl):
    dct_= {}
    for i in range (len(num_opl)):
        if num_opl[i].isdigit and num_opl[i] != '-' and num_opl[i] != '+':
            dct_ [num_opl[i][1::]] = num_opl[i][0]
            if num_opl[i-1] == '-':
                dct_ [num_opl[i][1::]] = ('-' + num_opl[i][0])      
    return dct_

with open ('mult_num1.txt', 'r') as file1:
    mult1=(file1.readlines())
print(str(mult1))
with open ('mult_num2.txt', 'r') as file2:
    mult2=(file2.readlines())
print((mult2))

dct_opl_1 = (opl(str_mult(mult1)))
dct_opl_2 = (opl(str_mult(mult2)))
for i in dct_opl_1:
    if i in dct_opl_2.keys():
        dct_opl_1[i] = (int(dct_opl_1[i]) + int(dct_opl_2[i]))
str_=''
for key, value in dct_opl_1.items():
    if value > 0:
        str_ = str_ + '+' + str(value) + str(key)
    else:
        str_ = str_ + str(value) + str(key)
with open ('result.txt', 'w') as file3:
    file3.write(str_)
