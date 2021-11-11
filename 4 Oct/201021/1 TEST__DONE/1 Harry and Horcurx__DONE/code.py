# https://6793fdf6.widgets.sphere-engine.com/lp?hash=bGymsTNze8

from typing import DefaultDict
n = int(input())
arr1 = [int(x) for x in input().split()]


odd_c = [0]
evene_c = [0]
for i in range(n):
    if arr1[i]%2==0:
        evene_c.append(evene_c[-1] + 1)
        odd_c.append(odd_c[-1])
    else:
        odd_c.append(odd_c[-1] + 1)
        evene_c.append(evene_c[-1])

d = DefaultDict(int)
d[0] = 1
ans = 0

for i in range(1,n+1):
    diff = odd_c[i] - evene_c[i]
    ans+=d[diff]

    d[diff] += 1
print(ans)
