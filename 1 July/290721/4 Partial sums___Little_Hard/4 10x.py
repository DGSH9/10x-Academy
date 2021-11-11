n, x = map(int, input().split())
arr = list(map(int, input().split()))

sum_of_aar = sum(arr)

res = 0
for i in arr:
    if sum_of_aar-i == x:
        res = 1
        break
print(res)
