t = int(input())
for i in range(t):
    arr1 = list(map(int,input().split()))
    maxi = 0
    sz = len(arr1)
    arr1.sort(reverse=True)

    for i in range(sz-2):
        if arr1[i]<(arr1[i+1] + arr1[i+2]):
            maxi = max(maxi,arr1[i] + arr1[i+1] + arr1[i+2])
            break
    if maxi==0:
        print(0)
    else:
        print(maxi)