n,k = map(int,input().split())
arr=list(map(int,input().split()))
temp=arr[k-1]
arr[k-1]=arr[n-k]
arr[n-k]=temp
for i in arr:
    print(i,end= " ")