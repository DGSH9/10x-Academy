arr1 = list(map(int, input().split()))
m = int(input())
x = m % len(arr1)
for i in range(len(arr1)):
    print(arr1[(x+i) % len(arr1)])
