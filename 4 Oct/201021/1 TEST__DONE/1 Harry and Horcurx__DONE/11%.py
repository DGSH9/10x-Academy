def hrho(n,arr1):
    d = 0
    res = 0
    p = [0]*(n+1)
    ne = [0]*(n+1)
    p[0]=1

    for i in range(n):
        if arr1[i] == 1:
            d+=1
        else:
            d-=1
        if(d<0):
            res+=ne[-d]
            ne[-d] = ne[-d]+1
        else:
            res+=p[d]
            p[d] = p[d]+1
        
    return res
n = int(input())
arr1 = list(map(int,input().split()))
print(hrho(n,arr1))