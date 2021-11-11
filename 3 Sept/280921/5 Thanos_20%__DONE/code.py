# https://6793fdf6.widgets.sphere-engine.com/lp?hash=r50whUPwcH

def f(arr,n):
    i=0
    j=len(arr)-1
    while(i<=j):
        mid=(i+j)//2
        if(arr[mid]==n):
            return mid
        elif(arr[mid]<n):
            i=mid+1
        else:
            j=mid-1
    return 0
n = int(input())
arr = list(map(int,input().split()))
t = int(input())
arr.sort()
# arr = list(OrderedDict.fromkeys(arr))
brr = list(map(int,input().split()))
for i in range(t):
    print(f(arr,brr[i])+1)  