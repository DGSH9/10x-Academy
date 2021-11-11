arr_size=int(input())
arr=list(map(int,input().split()))
minIndex=arr[0]
maxIndex=arr[1]
for i in range(arr_size):
    if arr[i]<minIndex:
        minIndex=arr[i]
for i in range(arr_size):
    if arr[i]>maxIndex:
        maxIndex=arr[i]
ans=maxIndex-minIndex
print(ans)



#################################  10x  #############
n=int(input())
l=list(map(int,input().split()))
maxi = l[0]
mini = l[0]
for i in l:
    maxi = max(l,i)
    mini = min(l,i)
print(maxi- mini)
