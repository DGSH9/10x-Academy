n=int(input())
arr1=list(map(int,input().split()))

arr1.sort()
arr2 = []
for i in range(len(arr1)):
    if arr1[i] not in arr2:
        arr2.append(arr1[i])
    
for i in range(0,2):
    print(arr2[i],end=" ")