n=int(input())
l =[]
for i in range(n):
    l.append(int(input()))

sum1 = 0
cnt = 0
for i in range(n):
    if(int(input())>2):
        sum1+=l[i]
        cnt+=1

if(cnt==0):
    print(-1)
else:
    print(sum1//cnt)