# принципы работы с файлами
from pathlib import Path

# current_dir = Path.cwd()
# #print(current_dir)
# file = open('data/text.txt','w')
# # 'w' перезапись файла, open если нет файла - создаст
# # 'a' добавляет текст в уже имеющийся файл
# file.write(str(current_dir))

# file.close()

# data = input("Введите текст: ")
# file = open('data/log.txt','a')
# file.write(str(data) + '\n')
# file.close()

file = open('data/log.txt','r')
# 'r' -для чтения
#print(file.read(5)) # только 5 символов выведется

for line in file:
    if not line == "" and not line == '\n' and not line == '\r\n':
        print(line,end = "")

file.close()
