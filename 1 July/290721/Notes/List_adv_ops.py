from functools import reduce

list1 = [1,2,6,3,4,8,9,65,7,4,23]

def addtoNumbers(x, y):
    return x+y
s = addtoNumbers(2, 5)
print(s)


addtoNumbers2 = lambda x, y :x + y
s2 = addtoNumbers2(10,5)
print(s2)


total = reduce(lambda x, y :x + y , list1)
print(total)























#---> FIlter function
list5 = [1,2,3,5,6,9,3,67,34,44,440,785,343,5467,25,67]
listerlist5 = filter(lambda x: x % 2 == 0,list5)
print(list(listerlist5))
listerlist5 = filter(lambda x: x >= 5,list5)
print(list(listerlist5))
