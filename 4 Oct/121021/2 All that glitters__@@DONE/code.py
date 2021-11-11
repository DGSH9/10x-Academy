# https://6793fdf6.widgets.sphere-engine.com/lp?hash=AziKGO9ytz
# https://6793fdf6.widgets.sphere-engine.com/lp?hash=AziKGO9ytz

def help1(carPrice,carQuality,n):
    arr1 = []
    for i in range(n):
        arr1.append((carPrice[i],carQuality[i]))
    # print(arr1)
    #sorting based on price and quality
    # arr1.sort(key=lambda x:x[1],reverse=True)
    # print(arr1)
    arr1.sort(key=lambda x:x[1])
    # print(arr1)

    for i in range(1,n):
        if arr1[i][1] < arr1[i][0]:
            # print(arr1[i])
            return 'Mark'
    return 'Lucy'

n = int(input())
carPrice = list(map(int,input().split()))
carQuality = list(map(int,input().split()))
print(help1(carPrice,carQuality,n))