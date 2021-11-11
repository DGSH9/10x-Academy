def maxSumPath(mtx,n,m):
    res = -1
    for j in range(n):
        res = max(res,mtx[0],j)

    for i in range(1,n):
        for j in range(m):
            if j>0 and j<m-1:
                mtx[i][j]=mtx[i][j] + max(mtx[i-1] [j-1],mtx[i-1],[j])
            elif(j==0):
                mtx[i][j]=mtx[i][j] + max(mtx[i-1] [j],mtx[i-1],[j+1])
            else:
                mtx[i][j]=mtx[i][j] + max(mtx[i-1] [j-1],mtx[i-1],[j])
    return res

mtx = [[1,2,3],
       [7,8,9],
       [4,5,6]]
print(maxSumPath,3,3)