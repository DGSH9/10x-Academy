# Operators

# ---> +
list1 = [False, 2]
list2 = [100, "Hello"]
list3 = list1 + list2 + [1, 2]
print(list3)

# ---> *
list4 = list1*100
list5 = [False]*1000
print(list5)

# ---> in operator
print(100 in [1, 2, 3, 4, 5])  # it will show false if present then shoow true
print(100 not in [1, 2, 3, 4, 5])
print(2 not in [1, 2, 3, 4, 5])

print(100 in list1)
print(100 in list2)
print(100 in list4)
