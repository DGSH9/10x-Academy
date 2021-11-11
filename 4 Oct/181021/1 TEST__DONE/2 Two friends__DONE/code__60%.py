# https://6793fdf6.widgets.sphere-engine.com/lp?hash=FFFUh2cf4j

n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

arr3 = []
for i in range(len(arr1)):      #time = nXn
    if(arr1[i] not in arr2):    #nlogn =>two pointer
        arr3.append(arr1[i])

for i in range(len(arr2)):      #time = nxn
    if(arr2[i] not in arr1):
        arr3.append(arr2[i])
arr3.sort()
for i in arr3:
    print(i)