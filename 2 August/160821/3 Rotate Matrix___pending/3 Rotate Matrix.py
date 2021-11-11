n = int(input())
matrix1 = [[int(x) for x in input().split()] for j in range(n)]
row, col = len(matrix1), len(matrix1[0])
res = []
for j in range(col):
    temp = []
    for i in range(row):
        temp.append(matrix1[i][j])
    res.append(temp[::-1])

print(len(res))
[print(*i) for i in res]
