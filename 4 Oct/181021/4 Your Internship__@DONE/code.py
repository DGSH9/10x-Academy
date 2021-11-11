# https://6793fdf6.widgets.sphere-engine.com/lp?hash=RqtHDihsUf

def Inter(n,k):
    res = 1
    while(n>=k):
        res = res*k
        n = n/k
    return res

for i in range(int(input())):
    n,k = map(int,input().split())
    print(Inter(n,k))