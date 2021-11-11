# https://6793fdf6.widgets.sphere-engine.com/lp?hash=frapJKNiKt

# priority 1 =>greater number of 2's
# priority 2 =>greater number

n = int(input())
arr1 = list(map(int,input().split()))

arr1.sort(reverse=True)
arr1.sort(key=lambda x:(str(x).count('2')),reverse=True)
for i in arr1:
    print(i,end=" ")