"""
Problem = First occurance of an element in given dataset
input   = [1,3,3,3,3,3,5]
output  = 3 : 4 (index of ifrst occurance)

"""


def binarySearch(arr1,left,right,element):
    possible = -1
    while(left<=right):
        mid = left+ (right - left)//2 # to avoid integer overflow
        if(arr1[mid])==element:
            possible = mid
            left = mid + 1
        elif(arr1[mid]>element):
            right = mid-1
        else:
            left = mid+1
    return possible

arr1 = [1,3,3,3,3,4,5]
left = 0
right = len(arr1)-1
element = 3
ans = binarySearch(arr1,left,right,element)
if(ans ==-1):
    print("element not present")
else:
    print(ans)