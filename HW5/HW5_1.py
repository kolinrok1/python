1 Напишите программу, удаляющую из файла все слова, содержащие "абв".

def serch (text_s):
    for i in range (len(text_s)):    
        if text_s[i:i+3] == 'абв':
            return True

with open ('D:\puthon_2\hw5\HW5_1.txt', 'r', encoding='utf=8') as file:
    text=(file.read())
with open ('D:\puthon_2\hw5\HW5_1.txt', 'w', encoding='utf=8') as file:
     file.write('')
text_list = list(text.split(' '))
for value in text_list:
    if serch (value) != True:
       with open ('D:\puthon_2\hw5\HW5_1.txt', 'a', encoding='utf=8') as file:
            file.write(value + ' ')
