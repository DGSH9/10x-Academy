n,m = list(map(int,input().split()))
arr = []
for i in range(n):
    x = list(map(int,input().split()))
    arr.append(x)
ans = 0
for i in range(n):
    for j in range(m):
        if(arr[i][j]%2!=0):
            ans+=arr[i][j]
print(ans)