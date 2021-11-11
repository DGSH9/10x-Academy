# https://6793fdf6.widgets.sphere-engine.com/lp?hash=i5F3fgdOSf

"""
| Ai+Aj|
9 8 -10 8 7 -6 1   => -10 -6 0 7 8 8 9   sort the array

"""

n = int(input())
arr1 = list(map(int,input().split()))
arr1.sort()

left ,right = 0,len(arr1)-1
left_val,right_val = None,None

mini = float('inf')

while(left < right):
    diff = arr1[left] + arr1[right]
    if(abs(diff) < mini):
        mini = abs(diff)
        left_val = arr1[left]
        right_val = arr1[right]

    if diff == 0:
        break
    if diff < 0:
        left+=1
    else:
        right-=1
print(left_val,right_val,mini)


