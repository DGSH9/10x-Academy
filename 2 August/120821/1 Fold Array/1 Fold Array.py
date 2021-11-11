import array
n = int(input())
ans = 0
for i in range(n):
    x = int(input())
    if(i == 0):
        ans += x
    else:
        if(i % 2 != 0):
            ans += x
        else:
            ans -= x
print(ans)
