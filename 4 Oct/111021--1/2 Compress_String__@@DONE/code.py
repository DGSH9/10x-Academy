# https://6793fdf6.widgets.sphere-engine.com/lp?hash=xgtur8afvC
def compress(st):
    ans  = ""
    count = 1
    ans +=st[0]

    for i in range(1,len(st)):
        if st[i] == st[i-1]:
            count+=1
        else:
            if count>1:
                ans += str(count)
            count = 1
            ans += st[i]

    if count > 1 :
        ans += str(count)
    print(ans)


    ## Complete this function.

t = int(input())
for _ in range(t):
    st = input()
    compress(st)