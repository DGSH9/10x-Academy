# https://6793fdf6.widgets.sphere-engine.com/lp?hash=5ZLP53ybyF

n = int(input())
arr1 = list(map(int,input().split()))

arr1.sort()
ans = 0
for i in range(0,len(arr1),2):
    ans += arr1[i]
print(ans)


# https://6793fdf6.widgets.sphere-engine.com/lp?hash=5ZLP53ybyF