# Given an integer matrix of size N * M. Find the maximum path sum in matrix.
# The maximum path is sum of all elements from first row to last row
# where you are allowed to move only down or diagonally to left or right.

# Input : mat[][] = 10 10  2  0 20  4
#                    1  0  0 30  2  5
#                    0 10  4  0  2  0
#                    1  0  2 20  0  4
# Output : 74
# The maximum sum path is 20-30-4-20.

# Input : mat[][] = 1 2 3
#                   9 8 7
#                   4 5 6
# Output : 17
# The maximum sum path is 3-8-6.

# n = r, m = c
def maxPathSum(mtx, n, m):
    res = -1
    # Iterate row 1
    for j in range(m):
        res = max(res, mtx[0][j])
    # Iterating over row 2 to last row
    for i in range(1, n):
        for j in range(m):
            # All three position above
            if j > 0 and j < m - 1:
                mtx[i][j] = mtx[i][j] + \
                    max(mtx[i - 1][j - 1], mtx[i - 1][j], mtx[i - 1][j + 1])
            elif j == 0:
                mtx[i][j] = mtx[i][j] + max(mtx[i - 1][j], mtx[i - 1][j + 1])
            else:
                mtx[i][j] = mtx[i][j] + max(mtx[i - 1][j - 1], mtx[i - 1][j])

            res = max(res, mtx[i][j])
    return res

mtx = [[10, 10,  2,  0, 20,  4],
       [1,  0,  0, 30,  2,  5],
       [0, 10,  4,  0,  2,  0],
       [1,  0,  2, 20,  0,  4]]
print(maxPathSum(mtx, 4, 6))

# mtx = [[1, 2, 3],
#         [7, 8, 9],
#         [4, 5, 6]]

#    [[10, 10, 2, 0, 20, 4],
#     [11, 10, 10, 50, 22, 25],
#     [11, 21, 54, 50, 52, 25],
#     [22, 54, 56, 74, 52, 56]]

# 1, 2, 3, 4
# 4, 10, 10, 10
# 3, 2, 30, 60
# 199, 40, 20, 20

# 1, 2, 3, 4
# 6, 13, 14, 14
# 16, 16, 44, 74
# 215, 84, 94, 74

# print(mtx)

# Total Time =  n * m
