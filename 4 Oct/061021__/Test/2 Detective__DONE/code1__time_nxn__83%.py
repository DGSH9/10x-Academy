# https://6793fdf6.widgets.sphere-engine.com/lp?hash=BVnzg4wFto

for i in range(int(input())):
    x = input()
    y = input()
    arr1 = list(x)
    arr2 = list(y)
    
    flag = 0
    for i in arr2:
        if i in arr1:
            pass
        else:
            flag = 1
    if flag == 0:
        print('YES')
    else:
        print("NO")