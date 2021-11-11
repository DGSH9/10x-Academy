a1, a2, a3 = list(map(int, input().split()))
b1, b2, b3 = list(map(int, input().split()))

AB = a1 * b1 + a2 * b2 + a3 * b3
A_B = (a2 * b3 - a3 * b2)**2 - (a1 * b3 - b1 * a3)**2 + (a1 * b2 - a2 * b1)**2
if AB == 0:
    print(2)
elif A_B == 0:
    print(1)
else:
    print(0)