# https://6793fdf6.widgets.sphere-engine.com/lp?hash=hPbo8TlRrZ

n = int(input())
arr1 = list(map(int,input().split()))
x = int(input())

s1 = set()
for i in range(len(arr1)):
    if arr1[i]==x:
        s1.add(i)

if len(s1)==0:
    print("-1",'-1')
else:
    print(*s1)
