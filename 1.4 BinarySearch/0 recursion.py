"""
BinarySearch(arr1,left,right,element)
    while(left<=right):
        calculate mid
        check with mid -->if arr1[mid] == element:
            return arr1[mid]
        
        check -->if arr1[mid] > element:
            right = mid-1
        
        check -->if arr1[mid] < element:
            left = mid + 1
    
    return -1


"""

def binarySearch(arr1,left,right,element):
    if(left<=right):
        mid = left+ (right - left)//2 # to avoid integer overflow
        if(arr1[mid])==element:
            return mid
        if(arr1[mid]>element):
            binarySearch(arr1,left,mid-1,element)
        else:
            binarySearch(arr1,mid+1,right,element)
    return -1


arr1 = [2,3,10,4]
left = 0
right = len(arr1)-1
element = 10
ans = binarySearch(arr1,left,right,element)
if(ans ==-1):
    print("element not present")
else:
    print(ans)