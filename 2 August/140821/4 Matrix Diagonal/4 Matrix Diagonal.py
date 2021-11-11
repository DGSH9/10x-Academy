
def change_diagonal(matrix):
    n = len(matrix)
    for i in range(n):
        j = i
        matrix[i][j]= (0 if matrix[i][j]<0 else 1)
    return matrix
# Do not change anything below this line.
if __name__ == "__main__":
    val = int(input())
    lst = []
    for index in range(0, val):
        lst.append([int(i) for i in input().split(' ')])
    out = change_diagonal(lst)
    for lst1 in out:
        print(" ".join(str(i) for i in lst1))