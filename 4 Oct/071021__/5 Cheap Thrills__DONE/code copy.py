# https://6793fdf6.widgets.sphere-engine.com/lp?hash=GHQKf4cIB2
# 1 2 3 => 3 2 1     => 0 cost
# 2 3   => 3 2       => 1 cost
for i in range(int(input())):
    n = int(input())
    arr1 = list(map(int,input().split()))   #  2 8 5 9 7
    ans = sorted(arr1)                      # [2 5 7 8 9]

    # two position => odd position and even position
    f = set()
    s = set()

    for i in range(0, n, 2): #chosing even group
        f.add(arr1[i])       #2 5 7
        s.add(ans[i])        #2 7 9

    diffent = f - s
    print(len(diffent))


# https://6793fdf6.widgets.sphere-engine.com/lp?hash=GHQKf4cIB2