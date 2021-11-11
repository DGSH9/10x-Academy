t = int(input())
for _ in range(t):
    st = input()
    ans = 0
    for i in range(len(st)):
        for j in range(i+1,len(st)+1):
            tmp = st[i:j]
            a = tmp.count('a')
            b = tmp.count('b')
            c = tmp.count('c')
            if(a==b):
                if(a==c):
                    if(len(tmp)>0):
                        ans+=1
    print(ans)