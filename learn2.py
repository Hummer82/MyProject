
# строки и их функции
#word = "itproger"
#print(word[1])
#print(word.count("p"),"; ",len(word))

#word="df,rt,gh,jk"
#hobby=word.split(",")

#for el in range(len(hobby)):
#    hobby[el] = hobby[el].capitalize()

#result=", ".join(hobby)

#print(result)

# индексы и срезы

#word="Football"
#print(word[0:4])
#print(word[1:-1:2]) # 2-шаг

#lis=[6,4,"Stroka",True,6.5]
#print(lis[2:5:2])
#print(lis[::-1])

# кортежи

#data = (4,6,7,3,6,True,5.6,"Hello") # можно и без скобок
##data[0]=5 # невозможно т.к. кортеж неизменяем
##print(data[1:5:2])
##print(data.count(6))

#for el in data:
#    print(el)

#nums=[4,6,2]
#new_data=tuple(nums) # преобразование списка в кортеж
#word= "Hello world!"
#new_data=tuple(word)
#print(new_data)

# словари

#country={4:3}

#country={"code":"RU",'name':'Russia','population':144}
#print(country['name'])
#print(country.items())

#for key, value in country.items():
#    print(key,' - ',value)

person = {
    'user_1':{
        'first_name':'John',
        'last_name':'Marley',
        'age':45,
        'address':['г. Москва','ул. Какая-то',45],
        'grades':{'math':5,'physics':3}
    },
    'user_2':{
    }
}

print(person['user_1']['address'][1])


# множества (set и frozenset)

#data = set('hello')
data = {5,3,7,4,5}
data.add(32)
data.update(['Hello',28,True,4])
data.remove(32)
#data.pop()
#data.clear()

nums=[9,0,12,30,0,0,30,9,9,9,0]
nums=set(nums) # удаляем автоматически все повторения

# frozenset - как кортеж неизменяемые множества
new_data = frozenset([5,3,7,4,5,'Hello',28,True,4,32,'32'])

print(new_data)

