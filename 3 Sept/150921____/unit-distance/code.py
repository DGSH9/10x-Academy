# https://6793fdf6.widgets.sphere-engine.com/lp?hash=eV9lRjXeWm

def isEditDistanceOne(string1, string2): 
    # Complete this function, and return True/False
    n = len(string1)
    m = len(string2)

    if (abs(n-m) > 1 or string1==string2):
        return False

    ed = 0    
    i = 0
    j = 0
    while(i<n and j<m):
        if string1[i]==string2[j]:
            i+=1
            j+=1
        elif(ed ==1):
            return False
        else:
            ed = 1
            if n>m:
                i+=1
            elif(m>n):
                j+=1
            else:
                i+=1
                j+=1
    return True

for _ in range(int(input())):
    input_string1, input_string2 = input().split()
    print(isEditDistanceOne(input_string1, input_string2))