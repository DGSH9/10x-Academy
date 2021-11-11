def AddSubstract(arr1,n,k):
    # base case
    if k == 0 and n == len(arr1):
        return 1
    if n >len(arr1):
        return 1
    # main case
    else:
        return( AddSubstract(arr1,n+1,k) + AddSubstract(arr1,n+1,k + arr1[n]) + AddSubstract(arr1,n+1,k - arr1[n]) )
        

if __name__ == '__main__':    
    k = int(input())
    n = int(input())
    arr1 = list(map(int,input().split()))[:n]
    print(AddSubstract(arr1,n,k))