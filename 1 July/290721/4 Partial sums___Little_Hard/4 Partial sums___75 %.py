n,k= map(int,input().split())
arr=list(map(int,input().split()))
sum=0
for i in arr:
    sum+=i
for i in range(len(arr)):
    last1=sum-arr[n-2]
    if(last1==k):
        print(1)
        break
    else:
        print(0)
        break