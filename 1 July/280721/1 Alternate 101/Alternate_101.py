n= map(int,input().split())
arr=list(map(int,input().split()))
sum=0
for i in range(len(arr)):
    if(i%2==0):
        sum+=arr[i]     
print(sum)