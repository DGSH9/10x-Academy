# https://6793fdf6.widgets.sphere-engine.com/lp?hash=Nw6Bh2Gy3t
from collections import defaultdict
n = int(input())
dict1 = {}        # name = game
dict1Like  = defaultdict(int)   # number of peoople llike the game
for i in range(n):
    name,game = input().split()
    if(name in dict1):
        continue
    
    else:
        dict1[name] = game
        dict1Like[game] += 1

maxLike = 0
maxGameLike = ""
for i in dict1Like:
    if(dict1Like[i] >= maxLike):
        maxLike=dict1Like[i]
        maxGameLike =  i
    elif dict1Like[i]==maxLike:
        if i < maxGameLike:
            maxGameLike = i
        
print(maxGameLike)
print(dict1Like['football'])


