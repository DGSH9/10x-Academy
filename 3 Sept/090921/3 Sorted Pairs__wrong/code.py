# https://6793fdf6.widgets.sphere-engine.com/lp?hash=S0UN2xmKtd
n = int(input())
arr1 = list(map(int,input().split()))

count = 0
for i in range(n):
    j = i
    for j in range(j,n):
        if arr1[i]>=arr1[j]:
            count+=1
print(count)


# (3,3) (3,5) (2,3) (2,5) (1,3) (1,5) (3,5).