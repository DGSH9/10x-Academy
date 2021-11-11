# https://6793fdf6.widgets.sphere-engine.com/lp?hash=8nFloeErdr

def intersect(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    i=0
    j=0
    arr = []
    while(i<n and j<m):
        if(nums1[i]==nums2[j]):
            arr.append(nums1[i])
            i+=1
            j+=1
        elif(nums1[i]<nums2[j]):
            i+=1
        else:
            j+=1
    if len(arr)==0:
        arr.append(-1)
    return arr


# DO NOT change anything below this line
if __name__ == "__main__":
    num1_len = int(input())
    nums1 = []
    for index in range(num1_len):
        nums1.append(int(input()))
    num2_len = int(input())
    nums2 = []
    for index in range(num2_len):
        nums2.append(int(input()))

    for element in intersect(nums1, nums2):
        print(element)