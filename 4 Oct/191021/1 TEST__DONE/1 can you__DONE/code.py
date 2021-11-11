# https://6793fdf6.widgets.sphere-engine.com/lp?hash=RjMmz1fmFy

from collections import defaultdict

for i in range(int(input())):
    n = int(input())
    ans1 = defaultdict(int)   #-->(x+y)
    ans2 = defaultdict(int)   #-->(x-y)
    for j in range(n):
        x,y = [int(k) for k in input().split()]

        ans1[x-y] +=1
        ans2[x+y] +=1

    ans = 0
    for i in ans1.values():
        ans+=(i*(i-1))//2
    
    for i in ans2.values():
        ans+=(i*(i-1))//2
    
    print(ans)