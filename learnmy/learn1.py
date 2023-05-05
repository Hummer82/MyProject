## -*- condig: utf-8 -*-
## Comment

# ctrl+K.C - закоментировать, обратно crtl+K,U

#print("Hello World")
## formating sep - сепаратор, разделитель между значениями, 
## end - оконцовка строки \n, \r... "" - объединит в одну строку со следующим принтом
#print("Result: ",7,15,".",sep=",",end="\n")
#print("Second line")
## sppetial
#print("Three \" line")
## mathfunc
#print("парапам:", 5+6)

## математические функции
#print("Результат:", min(5,6,0,-3,5))
## ввод ползователем
## переменные
#number=5 # int
#print("Результат = ", number)
##number=input("Введите число: ")
#digit=-5.456876 # float
#word="Результат: " # string
#print(word,digit)
#boolean=True # bool
## приведение типов
#print(word + str(digit))
#str_num='5'
#print(word, number + int(str_num))

#num1=int(input("Введите первое число: "))
#num2=int(input("Введите второе число: "))
#num1+=num1
#print("Результат: ", num1 + num2)
#print("Результат: ", num1 - num2)
#print("Результат: ", num1 / num2)
#print("Результат: ", num1 * num2)
#print("Результат: ", num1 ** num2)
#print("Результат: ", num1 // num2)
#word="Fr"
#print(word * num2)
#print("Type: ",type(word))
#word=-5.2158
#print("Type: ",type(word))

### условные операторы

#if 5 == 5:
#    print("Yes", end="")
#    print("!!!")

#user_data = int(input("Введите число: "))

##if user_data != 5:
##    print("Мы на месте")
##    if user_data > 6:
##        print("Number is bigger than 5")

#isHappy = True

#if not isHappy:
#    print("User is happy")
#elif isHappy and user_data == 6: # and - и, or - или
#    print("Happy: ", isHappy, " ", "User = ", user_data)
#elif user_data == 5 :
#    print("Number is 5")
#else:
#    print("User ia unhappy")
# тернарный оператор
#data = input()

#number = 5 if data == "Five" else 0

#print(number)

# циклы for, while. range - диапазон

#for i in range(1, 6, 2): # 1-начало диапазона, 6-конец диапазона, 2- шаг
#    print(i)

#word = "Hello World!"

#count = 0

#for i in word:
#    if i == "l":
#        count += 1
#print("Count: ", count)

#i = 1
#isHasCare = True

#while isHasCare or i < 3:
#    if input("Enter Data: ") == "Stop":
#        isHasCare = False
#    i += 1
#    print(i)

#for i in range(1, 11):
#    if i ==5:
#        break

#    if i % 2 ==0:
#        continue

#    print(i)

#found = None
#for i in "Hello":
#    if i == "l":
#        found = True
#        break
#    else:
#        found = False
#print(found)

# списки

#nums = [5,7,2,4,7, True,"Hello",6.7,[12,0.3]]

#nums[0]=50
#nums[5]=1

#print(nums)
#print(nums[:4])
#print(nums[-1][1])

#numbers=[5,2,7]
#numbers.append(100) # добавляет элемент в конец списка
#numbers.insert(1, True) # добавляет элемент в список по индексу
#numbers.extend([4.1,5,5]) # добавляет несколько элементов в конец списока
#numbers.sort() # сортировка
#numbers.reverse() # переворачивает лист
## numbers.pop()  удаление последнего элемента numbers
#numbers.remove(4.1) # удаление элемента по значению
#numbers.pop(0) # удаление элемента по индексу
##numbers.clear()  # удаление всех элементов списка
#print(numbers.count(5)) # подсчитывает колличество элементов в списке со значением 5
#print(len(numbers)) # размер списка
#print(numbers)

#nums=[5,2,7,"58",False]
#for el in nums:
#    el*=2
#    print(el)

n = int(input("Enter length: "))

user_list=[]
i=0
while i<n:
    string="Enter element #" + str(i+1) + ": "
    user_list.append(input(string))
    i+=1
print(user_list)



