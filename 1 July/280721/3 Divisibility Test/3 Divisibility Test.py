n,x= map(int,input().split())
arr=list(map(int,input().split()))
count=0
for i in range(len(arr)):
    if(arr[i]%x==0):
        count+=1        
print(count)