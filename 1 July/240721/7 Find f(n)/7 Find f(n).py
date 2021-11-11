n = int(input())
while(n > 0):
    sum1 = n*(n+1)//2
    req = (-1)**n*n
    ans = sum1//req
    print(ans)
    break
