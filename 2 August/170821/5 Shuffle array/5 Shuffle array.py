def shuffle(arr):
    # Implement this function
    arr2 = []
    arr3 = []
    s = len(arr)
    for i in range(0, s//2):
        arr2.append(arr[i])
    for i in range(s//2, s):
        arr3.append(arr[i])
    arr4 = []
    for i in range(len(arr2)):
        arr4.append(arr2[i])
        arr4.append(arr3[i])
    return arr4


# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    nums = []
    for index in range(2 * n):
        nums.append(int(input()))
    for elem in shuffle(nums):
        print(elem)
