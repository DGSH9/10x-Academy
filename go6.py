def findMissing(arr1, arr2, n, m):
    arr3=[]
    s = dict()
    for i in range(m):
        s[arr2[i]] = 1
 
    for i in range(n):
        if arr1[i] not in s.keys():
            arr3.append(arr1[i])
    return arr3

n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
print(findMissing(arr1, arr2, n, m))
