# https://6793fdf6.widgets.sphere-engine.com/lp?hash=XWPTxRWC5m

n = int(input())
arr1 = list(map(int,input().split()))

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0

for i in arr1:
    if i==1:
        c1+=1
    elif(i == 2):
        c2+=1
    elif(i==3):
        c3+=1
    elif(i==4):
        c4+=1
    elif(i==5):
        c5+=1

i = 0

while (c1 > 0):
    arr1[i] = 1
    i+=1
    c1-=1

while (c2 > 0):
    arr1[i] = 2
    i+=1
    c2-=1

while (c3 > 0):
    arr1[i] = 3
    i+=1
    c3-=1

while (c4 > 0):
    arr1[i] = 4
    i+=1
    c4-=1

while (c5 > 0):
    arr1[i] = 5
    i+=1
    c5-=1
print(*arr1)
