# https://6793fdf6.widgets.sphere-engine.com/lp?hash=Cf745JXn0V

# similar to => how we find min absolute diff between any two elements

# 5 4 7 8 1 => after sorting 1 4 5 7 8   => if difference of 1 and 5 is 4 then its not possible to diffof 4 and 5 is greater than is greater than 4

n,k=map(int,input().split())
arr1 = list(map(int,input().split()))
arr1.sort()

ans = float('inf') #define high value
for i in range(0,n-k+1):
    ans = min(ans,abs(arr1[i+k-1] - arr1[i]))
print(ans)
