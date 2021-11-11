t = int(input())
for i in range(t):
    n = int(input())
    arr1 = list(map(int,input().split()))
    
    arr1.sort()
    size = len(arr1)-1
    max_diff = arr1[size] - arr1[0]
    min_diff = arr1[1] - arr1[0]
    ans = max_diff * min_diff
    print (ans)