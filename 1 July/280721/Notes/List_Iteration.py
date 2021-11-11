list1 = [1, 2, 'j', False]

for element in list1:
    print(element)

# for r in range(len(list1)):
#     print(list1[r]

for indx, elem in enumerate(list1):
    print(indx, ",", elem)

i = 0
while i < len(list1):
    print(list1[i])
    i += 1

[print(list1[r]) for r in range(len(list1))]

# Operations in list
