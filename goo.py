def intersect(nums1, nums2):
    # implement this function
    arr1 = []
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            arr1.append(nums1[i])
    if len(arr1) ==0 :
        return [-1]
    else:
        return arr1

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