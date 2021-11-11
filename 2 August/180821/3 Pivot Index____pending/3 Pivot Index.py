def pivotIndex(arr):
    leftSum = 0
    rightSum = sum(arr) - arr[0]

    if leftSum == rightSum:
        return 0

    for i in range(1, len(arr)):
        leftSum += arr[i-1]
        rightSum -= arr[i]

        if leftSum == rightSum:
            return i
    return -1
    
# Do not edit anything below
if __name__ == "__main__":
    num_elems = int(input())
    nums = []
    for i in range(num_elems):
        nums.append(int(input()))

    print(pivotIndex(nums))
