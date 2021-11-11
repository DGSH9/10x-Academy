n=int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
arr.sort()
lower = 0
higher = n - 2
mid1 = 0
while (lower <= higher):
		mid1 = (lower + higher) // 2
		if (arr[mid1] == arr[mid1 ^ 1]):
			lower = mid1 + 1
		else:
			higher = mid1 - 1	
print(arr[lower])