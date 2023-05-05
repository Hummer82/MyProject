# Менеджер «With ... as» для работы с файлами
# try:
#     file = open("text.txt", "r")
#     file.read()
# except FileNotFoundError:
#     print("not found File")
# finally:
#     file.close() # будет ошибка т к file инициировани в блоке try
strFile = input("DIR File: ")
try:
    with open(strFile, 'r', encoding = 'utf-8') as file:
        strFile = file.name
        print("Файл: " + strFile + " - " + file.read())
    # with..as автоматически закроет файл без finally 
except FileNotFoundError:
    print("файл" + strFile + " не найден")


