# https://6793fdf6.widgets.sphere-engine.com/lp?hash=rX6fp6RVRr

"""
MAX
[1, 1, 3]
[4, 5, 6]


MIN
[1, 1, 3]
[6, 5, 4]

"""

n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr1.sort()
arr2.sort(reverse=True)

ans = 0
for i in range(n):
    ans+=arr1[i]*arr2[i]
print(ans)