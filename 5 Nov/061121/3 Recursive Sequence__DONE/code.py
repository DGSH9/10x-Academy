# https://6793fdf6.widgets.sphere-engine.com/lp?hash=xOL0XP0WOb
def f(i,j,n):
    if(i<=n):
        mul = 1
        for k in range(i):
            mul*=j
            j+=1
        return mul+f(i+1,j,n)
    else:
        return 0
for i in range(int(input())):
    print(f(1,1,int(input())))