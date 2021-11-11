n = int(input())
list1 = [int(input()) for value in range(n)]
dice = {}
maxi = 1
for value in list1:
    dice[value] = dice.get(value, 0)+1
    if(dice.get(value) > maxi):
        maxi = dice[value]

if(maxi > 1):
    for value in dice:
        if(dice.get(value) == maxi):
            print(value)
if(maxi == 1):
    print(-1)
