import math
n = int(input())
for i in range(n):
    value = math.factorial(n -1)//((math.factorial(n-i-1)) * math.factorial(i))
    print(value) 