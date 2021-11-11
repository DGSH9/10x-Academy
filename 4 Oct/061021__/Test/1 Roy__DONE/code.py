# https://6793fdf6.widgets.sphere-engine.com/lp?hash=DorieAiiJB

for i in range(int(input())):
    n = int(input())
    temp1 = 0 
    temp2 = ""

    for j in range(n):
        x = input()
        if x != x[::-1]:
            temp1 = 1
        temp2+=x

    if temp1 == 0:
        for j in range(n):
            x = temp2[j:n*n:n]
            if x != x[::-1]:
                temp1 = 1
                break
    if temp1 ==1:
        print("NO")
        continue
    else:
        print("YES")
