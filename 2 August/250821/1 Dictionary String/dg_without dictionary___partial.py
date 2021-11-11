n = input()
arr1 = list(map(str,input().split()))
arr2 = []
for i in range(len(arr1)):
    count=0
    f=0
    for j in arr1[i]:
        if j in n :
            count+=1
        else:
            f=1
    if(f==0):
        arr2.append(count)
# print(arr2)
arr2.sort()
print(arr2[len(arr2)-1])