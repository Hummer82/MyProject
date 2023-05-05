# функции (def.lambda)

#def test_func(word):
#    # pass - не выполнит ничего и выйдет
#    print(word,end="")
#    print('!')

#test_func("Hi")
#test_func(555)
#test_func(5.3)

#def summa(a,b):
#    res = a+b
#    print('Result: ',res)



#summa(45,54.2)
#summa('H','i')

#def summa(a,b):
#    res = a+b
#    return 'Result: ' + str(res)

#res = summa(45,54.2)
#print(res)
#res = summa('H','i')
#print(res)

#nums = [5,7,2,6,9,4]

#min = nums[0]
#for i in nums:
#    if i < min:
#        min = i

def minimal(l):
    min_number = l[0]
    for i in l:
        if i < min_number:
            min_number = i
    return min_number

print(minimal([5,7,2,6,9,4]))
print(minimal([5.3,7.4,2.6,2.1,6.9,9.4,4.0]))

print(minimal([minimal([5,7,2,6,9,4]),minimal([5.3,7.4,2.6,2.1,6.9,9.4,4.0])]))

# lambda - анонимная функция

func = lambda x, y: x * y
print(func(4,5))
