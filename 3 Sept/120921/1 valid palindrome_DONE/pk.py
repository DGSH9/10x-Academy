# https://6793fdf6.widgets.sphere-engine.com/lp?hash=T7sk7wQLwC
n = int(input())
for _ in range(n):
    st = input()
    ans=0
    i=0
    j=len(st)-1
    while(i<j):
        if(st[i]==st[j]):
            i+=1
            j-=1
        else:
            if(st[i+1]==st[j]):
                ans+=1
                i+=2
                j-=1
            elif(st[i]==st[j-1]):
                ans+=1
                i+=1
                j-=2
            else:
                ans+=1
                i+=1
                j-=1
    if(ans<=1):
        print("True")
    else:
        print("False")
        
