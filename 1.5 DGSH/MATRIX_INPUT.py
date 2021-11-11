"""METHOD-1"""
n = int(input())
m = int(input())
matrix = [[int(x) for x in input().split()] for k in range(m)]
print(matrix)


"""method-2"""
n  = int(input())
m  = int(input())

matrix = []
for i in range(n):
    arr1 = []
    for j in range(m):
        x = int(input())
        arr1.append(x)
    
    matrix.append(arr1)
print("==>",matrix[0][0])
