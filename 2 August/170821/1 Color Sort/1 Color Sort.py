n = int(input())
arr1 = []
for i in range(n):
    arr1.append(int(input()))
c0 = 0
c1 = 0
c2 = 0
for i in range(len(arr1)):
    if(arr1[i] == 0):
        c0 += 1
    if(arr1[i] == 1):
        c1 += 1
    if(arr1[i] == 2):
        c2 += 1
for i in range(c0):
    print(0)
for i in range(c1):
    print(1)
for i in range(c2):
    print(2)
