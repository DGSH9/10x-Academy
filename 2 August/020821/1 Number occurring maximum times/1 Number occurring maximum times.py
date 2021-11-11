n = int(input())
arr1 = []
for i in range(n):
    x=int(input())
    arr1.append(x)
brr = []
for i in range(len(arr1)):
    x=arr1.count(arr1[i])
    if(x==4):
        brr.append(arr1[arr1[i]])
        break
if(len(brr)>0):
    for i in brr:
        print(i)
else:
    print(-1)