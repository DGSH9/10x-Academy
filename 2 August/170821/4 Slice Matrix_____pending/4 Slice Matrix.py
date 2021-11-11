m, n = list(map(int, input().split()))
arr = []
for i in range(m):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

a, b, x, y = list(map(int, input().split()))
for i in range(x, y+1):
    for j in range(a, b+1):
        print(arr[i-1][j-1], end=' ')
    print()
