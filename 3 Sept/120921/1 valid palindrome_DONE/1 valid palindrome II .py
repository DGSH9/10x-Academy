def palin(str1):
    mismatch = 0
    start = 0
    end = len(str1)-1
    flag1 = 0
    while start < end:
        if str1[start] != str1[end]:
            mismatch += 1
            if mismatch <= 1:
                start += 1  # trying deliting start at 1
            else:
                flag1 += 1
                break
        else:
            start += 1
            end -= 1

    mismatch = 0
    flag2 = 0
    while start < end:
        if str1[start] != str1[end]:
            mismatch += 1
            if mismatch <= 1:
                end -= 1  # tring deliting end at 1
            else:
                flag2 += 1
                break
        else:
            start += 1
            end -= 1

    if flag1 == 0 or flag2 == 0:  # return True if either of them is True
        return True
    elif(flag2 == 1 or flag2 == 1):
        return False


for i in range(int(input())):
    str1 = input()
    print(palin(str1))
