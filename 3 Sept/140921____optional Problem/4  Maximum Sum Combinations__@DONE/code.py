# https://6793fdf6.widgets.sphere-engine.com/lp?hash=LevLEfgyc3

n = int(input())
arr1 = list(map(int,input().split()))

arr1.sort(reverse=True)
a = 0
b = 0
for i in range(len(arr1)):
    if i%2==0:
        a = a * 10 + arr1[i]
    else:
        b = b*10+arr1[i]

print(a+b)