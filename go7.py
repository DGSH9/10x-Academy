
n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
print(findMissing(arr1, arr2, n, m))

arr3=[]
s = dict()
for i in range(m):
    s[arr2[i]] = 1

for i in range(n):
    s[arr1[i]] = 1

for i in range(n):
    if arr1[i] not in s.keys():
        # print(a[i], end = " ")
        arr3.append(arr1[i])

for i in range(n):
    if arr2[i] not in s.keys():
        # print(a[i], end = " ")
        arr3.append(arr2[i])



arr3 = []
for i in range(len(arr1)):     
    if(arr1[i] not in arr2):   
        arr3.append(arr1[i])

for i in range(len(arr2)):    
    if(arr2[i] not in arr1):
        arr3.append(arr2[i])
arr3.sort()
for i in arr3:
    print(i)