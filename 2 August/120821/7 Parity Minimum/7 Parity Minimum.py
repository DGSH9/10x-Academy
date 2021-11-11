n = int(input())
arr1 = []
for i in range(n):
    x = int(input())
    arr1.append(x)

min_value = min(arr1)
sum = 0
for digit in str(min_value):
    sum += int(digit)
if(sum % 2 != 0):
    print(0)
if(sum % 2 == 0):
    print(1)
