def minDiff(arr, n):
    ans = float('inf')
    arr.sort()
    for i in range(1,n):
        ans =min(ans, arr[i]-arr[i-1])
    return ans

def maxDiff(arr, n):
    return max(arr)-min(arr)
	
def prodDiff(arr, n):
	### Complete this and the above functions!
    if(length<=1):
        return "NA"
    return maxDiff(arr,n)*minDiff(arr,n)

for _ in range(int(input())):
    length = int(input())
    arr = [int(x) for x in input().split()]
    print(prodDiff(arr, length))

