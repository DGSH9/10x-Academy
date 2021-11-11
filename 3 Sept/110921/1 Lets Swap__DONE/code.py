# https://6793fdf6.widgets.sphere-engine.com/lp?hash=nG2BcpPWxT
n = int(input())
arr1 = list(map(int,input().split()))

mini = []
maxi = []
res = 0
for i in range(n):
    res += abs(i+1 - arr1[i])
    mini.append(min(arr1[i],i+1))
    maxi.append(max(arr1[i],i+1))

res += 2*(abs(max(mini) - min(maxi)))
print(res)