def sumofdivisors(n):
    i = 1
    sum1 = 0
    while i <= n:
        if (n % i == 0):
            sum1 += i
        i = i + 1
    return sum1
n = int(input())
print(sumofdivisors(n))
