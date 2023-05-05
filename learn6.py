#  обработчик исключений

# try:
#     x = int(input("Введите число: "))
#     x += 5
#     print(x)
# except ValueError:
#     print("Введите лучше число")

# x = 0
# while x == 0:
#     try:
#         x = int(input("Введите число: "))
#         x += 5
#         print(x)
#     except ValueError:
#         print("Введите лучше число")

y = 0
try:
    x = int(input("Enter dijit: "))
    y = 5 / x
except ZeroDivisionError:
    print("Деление на 0")
except ValueError:
    print("Only dijit")
else:
    print("Else если нет искл. сработает")
finally:
    print("Finally: y = " + str(y) + " сработает всегда")

