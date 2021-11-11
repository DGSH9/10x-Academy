n,k = list(map(int,input().split()))
arr = [0]*k
i=0
while(n!=0):
    arr[i%k]+=1
    i+=1
    n-=1
# print(arr)
print(max(arr)-min(arr))