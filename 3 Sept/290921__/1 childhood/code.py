# https://6793fdf6.widgets.sphere-engine.com/lp?hash=K5kufyFAGV

n = int(input())
for i in range(n):
    a,b = map(str,input().split())
    
    st = input()

    arr1 =list(st)
    # print(arr1)
    i1 = 0
    i2 = 0
    for i in range(len(arr1)):
        if arr1[i] == a:
            i1 = i
        if arr1[i]== b:
            i2 = i
    # for i in range(n):
    if arr1[i1].isupper() and arr1[i2].isupper():
        arr1[i1],arr1[i2] = arr1[i2],arr1[i1]
    elif arr1[i1].isupper() and arr1[i2].islower():
        arr1[i1].lower() and arr1[i2].upper()
        arr1[i1],arr1[i2] = arr1[i2],arr1[i1]

    elif arr1[i1].islower() and arr1[i2].isupper():
        arr1[i1].upper() and arr1[i2].lower()
        arr1[i1],arr1[i2] = arr1[i2],arr1[i1]
    else:
        arr1[i1],arr1[i2] = arr1[i2],arr1[i1]

    for i in arr1:
        print(i,end="")