n = int(input())
c = 0
for _ in range(n):
    arr = list(map(int,list(input())))
    sm = sum(arr)
    pro  = 1
    for i in arr:
        pro*=i
    if(sm>=pro):
        c+=1
print(c)