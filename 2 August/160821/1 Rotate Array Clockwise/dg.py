arr1 = list(map(int, input().split()))
m = int(input())
arr2 = []
for i in range(len(arr1)):
    x = m % len(arr1)
for j in range(x, len(arr1)):
    arr2.append(arr1[j])
for k in range(0, x):
    arr2.append(arr1[k])
for i in range(len(arr2)):
    print(arr2[i])
