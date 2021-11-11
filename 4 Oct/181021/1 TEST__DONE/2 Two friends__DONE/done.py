# https://6793fdf6.widgets.sphere-engine.com/lp?hash=FFFUh2cf4j
n= int(input())
f1 = set([int(x) for x in input().split()])
m =int(input())
f2 = set([int(x) for x in input().split()])

ans1 = f1.difference(f2)
ans2 = f2.difference(f1)
ans = list(ans1)+list(ans2)
ans.sort()
for i in ans:
    print(i)