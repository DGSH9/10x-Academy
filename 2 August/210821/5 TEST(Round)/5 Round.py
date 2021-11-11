def roundIt(arr1, length):
    if(length <= 1):
        return [-1]

    ans = []
    for i in range(length-1):
        if(arr1[i] == 0):
            return [-1]
        ans.append(round(arr1[i+1]/arr1[i]))
    return ans


for _ in range(int(input())):
    length = int(input())
    arr1 = [int(x) for x in input().split()]
    print(*roundIt(arr1, length))
