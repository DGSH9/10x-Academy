def Factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


num = int(input())
if(num < 0):
    print('undefined')
else:
    print(Factorial(num))
