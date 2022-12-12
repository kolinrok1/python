def zip_ (text_unzip):
    count_ = 0
    zip_txt = ''
    find_char = text[0]
    for i in range(len(text)):
        if text_unzip[i] == find_char:
            count_ += 1
        else:
            zip_txt += str(count_) + find_char 
            find_char = text_unzip[i]
            count_ = 1
    return(zip_txt)

def unzip_ (text_zip):
    unzip_txt = ''
    per_char = 0
    for i in range(len(text)):
        if text_zip[i].isdigit():
            per_char = text_zip[i]
        else:
            unzip_txt += int(per_char) * str(text_zip[i])
    return(unzip_txt)

with open ('D:\puthon_2\hw5\zip.txt', 'r', encoding='utf=8') as file:
    text=(file.read() + ' ')
print(text)
zip_unzip = input('Вы хотели сжать текст или распаковать: \n 1 - распаковать.\n 2 - зжать\n Введите цифру: ')
if zip_unzip == '1':
    text= unzip_(text)
elif zip_unzip == '2':
    text= zip_(text)

with open ('D:\puthon_2\hw5\out_zip.txt', 'w', encoding='utf=8') as file:
    file.write(text)
