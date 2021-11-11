# https://6793fdf6.widgets.sphere-engine.com/lp?hash=IdV3WZXLt3
def zeroSum(matrix, rows, cols):
    res = 0

    for i in range(rows):
        sum = 0
        for j in range(cols):
            sum += matrix[i][j]
        if sum == 0:
            res +=1
    
    for i in range(cols):
        sum = 0
        for j in range(rows):
            sum +=matrix[j][i]
        
        if (sum == 0):
            res +=1
    
    return res



for _ in range(int(input())):
    n,m = map(int, input().split())
    arr = [[int(x) for x in input().split()] for i in range(n)]
    print(zeroSum(arr, n, m))