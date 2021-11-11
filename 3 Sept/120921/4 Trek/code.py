# https://6793fdf6.widgets.sphere-engine.com/lp?hash=jICmAHKzDG
def treck(n,steps):
    #altitude
    alt = 0
    valley = 0

    if steps[0]=='U':
        alt+=1
    else:
        alt-=1
    
    for i in range(1, n):
        if steps[i]=='U':
            alt+=1
        else:
            alt-=1
        if alt==0:
            if steps[i] =='U':
                valley+=1
    return valley

for i in range(int(input())):
    n = int(input())
    steps = input()
    print(treck(n,steps))