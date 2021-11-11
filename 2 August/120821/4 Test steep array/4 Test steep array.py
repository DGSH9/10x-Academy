n = int(input())
arr = list(map(int, input().strip().split()))[:n]
sum = 0
mx = arr[-1]
for i in range(n-1, -1, -1):
    mx = max(arr[i], mx)
    sum += mx-arr[i]
print(sum)