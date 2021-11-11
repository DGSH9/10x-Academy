# https://6793fdf6.widgets.sphere-engine.com/lp?hash=y6b2gMi20S

# https://6793fdf6.widgets.sphere-engine.com/lp?hash=y6b2gMi20S

def longest(str):
    if str=="":
        return 0
    last_occur = [-1]*256
    left = -1
    ans = 0
    for i in range(len(str)):
        left = max(left,last_occur[ord(str[i])])
        len_substr = i -left
        ans = max(ans,len_substr)

        last_occur[ord(str[i])]  = i

    return ans

for _ in range(int(input())):
    str = input()
    print(longest(str))