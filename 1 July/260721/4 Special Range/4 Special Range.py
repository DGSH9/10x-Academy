m = int(input())
n = int(input())
if(m<0):
    m=0
if n>=0:
    for i in range(m,n+1):
        print(i)
else:
    print(-1)