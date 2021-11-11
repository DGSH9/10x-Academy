# https://6793fdf6.widgets.sphere-engine.com/lp?hash=eV9lRjXeWm

def isEditDistanceOne(string1, string2): 
    # Complete this function, and return True/False
    l1 = len(string1)
    n= len(string2)
    if abs(l1 - n) > 1:
        return False
    count = 0 
    i = 0
    j = 0
    while i < l1 and j < n:
        if string1[i] != string2[j]:
            if count == 1:
                return False
            if l1 > n:
                i+=1
            elif l1 < n:
                j+=1
            else: # 
                i+=1
                j+=1
            count+=1
        else:
            i+=1
            j+=1
    if i < l1 or j < n:
        count+=1

    return count == 1

for _ in range(int(input())):
    input_string1, input_string2 = input().split()
    print(isEditDistanceOne(input_string1, input_string2))