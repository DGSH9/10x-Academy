import math

n = int(input())
sum2 = 0
x = list(map(int, input().split()))
for j in range(len(x)):
    sum2 = sum2+(math.ceil(x[j]*0.07))
print(sum2)
