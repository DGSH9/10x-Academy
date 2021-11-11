# https://6793fdf6.widgets.sphere-engine.com/lp?hash=4Gh2DBUxyD

for i in range(int(input())):
    s = input()
    dict1 = {}
    ans = -1
    for j in range(len(s)):
        if s[j] not in dict1:
            dict1[s[j]]=j
        else:
            dict1[s[j]]=-1
    for k in dict1:
        if (dict1[k] != -1):
            ans = dict1[k]
            break
    print(ans)