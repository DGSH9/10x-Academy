# https://6793fdf6.widgets.sphere-engine.com/lp?hash=ayR2mdOfaa

# 2 3          #1st is favour and 2nd is anger
# 10 2         #if choose favour happiness increase by 2 
# 11 5         #if choose anger happiness decrease by 3
# 4 1

# maximum happiness =   (hi + hj) - sumation(ak, k means all element except i and j)  
                    # these are happiness of ith girl and jth girl
                    # =(hi + hj) - sumation(ak, k means all element except i and j)   + ai + aj - ai - aj 
                    # = (hi + hj) - sumation(ak, k means all) + ai + aj
                    # =(hi + hj) + (hj + aj) - sumOfALlAnger

for _ in range(int(input())):
    n = int(input())
    sumOfALlAnger = 0
    arr1 = []
    for i in range(n):
        h,a = map(int,input().split())
        sumOfALlAnger += a
        arr1.append(h,a)
    arr1.sort(key = lambda x:(x[0] + x[1]),reverse=True)
    ans = arr1[0][0] + arr1[0][1] + arr1[1][0] + arr1[1][1] - sumOfALlAnger
    print(ans)
