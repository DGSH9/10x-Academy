n = int(input())
m = int(input())
arr1 = list(map(int, input().strip().split()))
arr2 = list(map(int, input().strip().split()))
for i in range(len(arr1)):
    if(arr1[i] < 0):
        arr1[i] = arr1[i]*-1

for i in range(len(arr2)):
    if(arr2[i] < 0):
        arr2[i] = arr2[i]*-1
mx1 = max(arr1)
mx2 = max(arr2)
print(mx1*mx2)
