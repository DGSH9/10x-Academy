# https://6793fdf6.widgets.sphere-engine.com/lp?hash=nDFykaAKwU

def GCD(a, b):
    if(b == 0):
        return a
    else:
        return GCD(b, a%b)
for i in range(int(input())):
    a,b = map(int,input().split())
    print(GCD(a,b))
