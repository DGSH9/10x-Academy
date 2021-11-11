n = int(input())
if(n == 0):
    print(-1)
else:
    arr = []
    for i in range(n):
        x = int(input())
        arr.append(x)
    max = 0
    for i in arr:
        fr = arr.count(i)
        if(fr > max):
            max = fr
    ans = []
    for i in arr:
        if(arr.count(i) == max):
            ans.append(i)
    ans = list(set(ans))
    for i in ans:
        print(i)
