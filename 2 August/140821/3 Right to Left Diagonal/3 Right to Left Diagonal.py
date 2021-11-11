def right_to_left_diagonal(matrix):
    result = []
    n = len(matrix)
    for i in range(n):
        j=n-1-i
        result.append(matrix[i][j])
    return result
if __name__ == "__main__":
    m = int(input())
    lst = []    
    for val in range(0, m):
        lst.append([int(i) for i in input().split(' ')])
    out = right_to_left_diagonal(lst)
    [print(val) for val in out]