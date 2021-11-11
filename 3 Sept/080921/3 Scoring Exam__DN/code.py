n,q = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr1.sort(reverse=True)
cum_time = [arr1[0]]

for i in range(1,n):
    cum_time.append(cum_time[-1] + arr1[i])

for i in range(q):
    x = int(input())
    print(cum_time[x-1])

    # https://6793fdf6.widgets.sphere-engine.com/lp?hash=m0OU6HNivY