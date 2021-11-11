# Search/find in a list

list1 = [100,200,300,400,500,600]
print(list1.index(100))
print(list1.index(600))

#--->Count
print("total 600 in give list are :",list1.count(600))
list1.index(500,2,5)
print(list1)


#--->copy
list2 = [11,22,33,44,55,66,77,88,99]

list3 = list1.copy()
print(list3)


# list4 = [["hellow",'Bye'],600,400,100]
# list5 = list4.copy()
# print(list4[0][0])

# list4[0][0] = 'world'
# print(list4)


#--->deepcopy  and shalow copy
import copy                    #used to import copy

x=["hellow", 'Bye']
list4 = [x,600,400,100]
list5 = list4.copy()

list6 = copy.deepcopy(list4)   #calling a method called deepcopy from copy library
print(x[0])
x[0] = "world"                 # change the value from list6 of indeex 0

print(list4[0][0])

# list4[0][0] = 'world'
print(list4)
print(list6)
