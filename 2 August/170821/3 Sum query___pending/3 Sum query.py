n,q =map(int,input().split())
arr1 = list(map(int,input().split()))

cum_sum = [arr1[0]]
for i in range(1,n):
    cum_sum.append(arr1[i] + cum_sum[-1])

for i in range(q):
    l,r = map(int,input().split())
    l,r = l-1,r-1

    if l-1>=0:
        print(cum_sum[r] - cum_sum[l-1])
    else:
        print(cum_sum[r])