# Модули. Создание и работа с модулями
# https://pypi.org

# import time
# time.sleep(3)
# print("Hi")

# import datetime as d

# print(d.datetime.now().time().hour())

# import sys, os, platform

# print(sys.path)
# print(os.name, platform.system())

# from math import sqrt as sq, ceil

# print(ceil(sq(100)))

import mymodul as mm
from mymodul import add_three_numbers as add

mm.hello()
mm.name = "Chack"

mm.hello()

print(add(7,8,9))