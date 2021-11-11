k = int(input())
n = int(input())
f=0
for i in range(n):
    x = int(input())
    if(x == k):
        f = 1
        print(i)
        break
if(f == 0):
    print(-1)
