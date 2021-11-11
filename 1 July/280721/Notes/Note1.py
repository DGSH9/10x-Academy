# Nested List

nestedList = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]]

len(nestedList)      # 4
len(nestedList[0])   # 5 n(row) x m(column) =
nestedList[0]        # [1,2,3,4,5]
print(nestedList[0])

nestedList[0][0]  # 1
nestedList[1][0]  # 6
nestedList[3][4]  # 20

x=nestedList[-1]
print(x)

print(nestedList[3])
print(nestedList[-1])

print(nestedList[3][4])
print(x[-1])

print(nestedList[-1][-1])
print(nestedList[-1][-5])


#Another way to represent nested list
a=[1,1,1,1,1,"Hellow"]
b=[1,1,21,32,43,54,"DGSH"]
c=[22,33,44,55,66]
d=[12,34,56,78,90]

nestedList[a,b,c,d]
print(nestedList)