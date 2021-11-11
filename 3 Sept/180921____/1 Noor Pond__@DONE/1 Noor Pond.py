for i in range(int(input())):
    sz = []
    fr = []
    N=int(input())
    for i in range(N):
        x,y = map(int, input().strip().split())
        sz.append(x)
        fr.append(y)
    sz.sort()
    fr.sort()
    count = N
    j = 0
    for i in range(N):
        if fr[i] >= sz[j]:
            count -= 1
            j += 1
    print(count)