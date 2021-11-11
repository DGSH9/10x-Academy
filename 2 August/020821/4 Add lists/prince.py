n = int(input())
for _ in range(n):
    arr = list(map(int, input().split(' ')))
    brr = list(map(int, input().split(' ')))
    m = len(arr)
    n = len(brr)
    arr.extend([0]*(max(m, n)-m))
    brr.extend([0]*(max(m, n)-n))
    c = 0
    ans = []
    for i in range(max(n, m)):
        ans.append(arr[i]+brr[i]+c)
        c = ans[i]//10
        ans[i] = ans[i] % 10
    if c > 0:
        ans.append(c)
    ans = list(map(str, ans))
    print(''.join(ans))
