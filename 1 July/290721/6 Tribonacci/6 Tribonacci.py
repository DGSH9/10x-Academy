size = int(input())
Tribonacci = [0, 0, 1]
for i in range(3, (size+1)):
    x = Tribonacci[i-1]+Tribonacci[i-2]+Tribonacci[i-3]
    Tribonacci.append(x)
print(Tribonacci[size-1])
