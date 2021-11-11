
def sumofproduct(n):
    # Code here
    result = 0
    for x in range(1, n + 1):
        y = n//x
        result = result + (y * x)
    return result


n = int(input())
print(sumofproduct(n))