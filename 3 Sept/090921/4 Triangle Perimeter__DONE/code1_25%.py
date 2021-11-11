# https://6793fdf6.widgets.sphere-engine.com/lp?hash=ClH5kF63r2
t = int(input())
for i in range(t):
    arr1 = list(map(int,input().split()))
    maxi = 0
    sz = len(arr1)
    for i in range(sz-2):
        for j in range(i+1,sz-1):
            for k in range(j+1,sz):
                a = arr1[i]
                b = arr1[j]
                c = arr1[k]
                if (a < b+c and b < a+c and c < a+b):
                    maxi = max(maxi,a+b+c)
    if maxi==0:
        print(0)
    else:
        print(maxi)