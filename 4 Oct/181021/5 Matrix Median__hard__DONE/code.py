# https://6793fdf6.widgets.sphere-engine.com/lp?hash=gvLuGDB32G
from bisect import bisect_right as upper_bound

MAX = 100
def mtrx(m, r, d):
    mi = m[0][0]
    mx = 0
    for i in range(r):
        if m[i][0] < mi:
            mi = m[i][0]
        if m[i][d-1] > mx :
            mx =  m[i][d-1] 
    desired = (r * d + 1) // 2
    while (mi < mx):
        mid = mi + (mx - mi) // 2
        place = [0]
        for i in range(r):
             j = upper_bound(m[i], mid)
             place[0] = place[0] + j
        if place[0] < desired:
            mi = mid + 1
        else:
            mx = mid
    return mi

for i in range(int(input())):
    n,m = list(map(int,input().split()))
    matrix = [[int(x) for x in input().split()] for k in range(n)]
    print(mtrx(matrix,n,m))