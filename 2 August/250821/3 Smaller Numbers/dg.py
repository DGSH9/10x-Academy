n = int(input())
# arr1 = list(map(int,input().split()))
arr1 = []
for i in range(n):
    arr1.append(int(input()))

# print(arr1)
arr2 = []
for i in arr1:
    arr2.append(i)
arr2.sort()
arr3 =[]
for i in range(len(arr1)):
    count = 0
    for j in range(len(arr2)):
        if(arr1[i]>arr2[j]):
            count+=1
    arr3.append(count)
# print(arr3)
for i in arr3:
    print(i)