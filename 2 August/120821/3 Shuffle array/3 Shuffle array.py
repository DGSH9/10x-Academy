import array
n = int(input())
arr1 = []
for i in range(2*n):
    x = int(input())
    arr1.append(x)

arr2 = []
arr3 = []
s = len(arr1)
for i in range(0,s//2):
    arr2.append(arr1[i])

for i in range(s//2,s):
    arr3.append(arr1[i])
for i in range(len(arr2)):
    print(arr2[i])
    print(arr3[i])