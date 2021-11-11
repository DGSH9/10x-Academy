#https://6793fdf6.widgets.sphere-engine.com/lp?hash=DlFv0CyFZj
def kang(x1,v1,x2,v2):
    if x1>x2 and v1>v2:
        return "NO"
    elif(x1<x2 and v1<v2):
        return "NO"
    
    if v1 ==v2:
        return "NO"
    if(x1-x2)%(v1-v2) == 0 or (x2-x1)%(v2-v1) == 0:
        return "YES"
    else:
        return "NO"
for i in range(int(input())):
    x1,v1,x2,v2 = map(int,input().split())
    print(kang(x1,v1,x2,v2))