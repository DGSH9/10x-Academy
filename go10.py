def f(arr1,n,x):
    start = 0
    end  = n-1
    ans = -1
    while(start <= end):
        mid = (start+end)//2

        if arr1[mid] == x:
            ans = mid           #to find first ocuurance
            end = mid-1
        elif(arr1[mid] > x):
            end = mid-1
        else:
            start = mid+1
    return ans


def l(arr1,n,x):
    start = 0
    end  = n-1
    ans = 1
    
    while(start <= end):
        mid = (start+end)//2

        if arr1[mid] == x:
            ans = mid
            start = mid+1
        elif(arr1[mid] > x):
            end = mid-1
        else:
            start = mid+1
    return ans


n = int(input())
arr1 = list(map(int,input().split()))
x = int(input())
print(f(arr1,n,x),l(arr1,n,x))