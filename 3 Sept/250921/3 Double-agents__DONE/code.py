# https://6793fdf6.widgets.sphere-engine.com/lp?hash=E1w6LaDSQw
n = int(input())
arr1 = list(map(str,input().split()))

ans = 0
dict1 = {}

for i in arr1:
    i = str(''.join(sorted(i)))
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1
    
    ans = max(ans,dict1[i])
print(ans)
    