import array
a = array.array("i",[1,2,3])
print(a)
print(type(a))


#################### ADD Operation ###################################
# 1.insert(index,value)    =>#O(n)
# 2.append(value)          =>O(1)

a.insert(0,100)    
print(a)
a.insert(3,300)
print(a)

a.append(1000)
print(a)

########################## Delete Operation #############################
#1.remove(valuw)   => O(n)
#2.pop(value) =>O(1) and pop(index,pop) => O(n)

a.remove(1)
print(a)
# a.remove(1)    #give error becoz index on already deletd (not present)
# print(a)

a.insert(0,1)
a.insert(0,1)
print(a)
a.remove(1)
print(a)

a.pop()            #=> It will remove last element
print(a)
a.pop(2)
print(a)

a.pop(3)
print(a)