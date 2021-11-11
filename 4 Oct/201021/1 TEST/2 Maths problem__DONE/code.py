# https://6793fdf6.widgets.sphere-engine.com/lp?hash=FucCausCdH

def gcd(a,b):
    if a%b==0:
        return b

    else:
        return gcd(b,a%b)

for i in range(int(input())):
    a,b=map(int,input().split())
    print(gcd(a,b))