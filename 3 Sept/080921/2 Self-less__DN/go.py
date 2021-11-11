for i in range(int(input())):
    n = int(input())
    arr1 = list(map(int, input().split()))

    sz = len(arr1)
    arr2 = [1] * sz
    left = 1
    for i in range(sz - 1):
        left *= arr1[i]
        arr2[i+1] *= left
    right = 1
    for i in range(sz-1, 0, -1):
        right *= arr1[i]
        arr2[i-1] *= right
    print(arr2)

# https://6793fdf6.widgets.sphere-engine.com/lp?hash=hjzJGLp4al