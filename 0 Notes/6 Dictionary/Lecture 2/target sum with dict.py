def twoNumberSum(arr1,targetsum):
    num = {}
    for i in arr1:
        secondNum = targetsum-i
        if(secondNum in num):
            return [i,secondNum]
        else:
            num[i] = True
    return []

# arr1 = [int(x) for x in input().split()]

# if __name__== "__main__":
testCase  = [([3, 5, -4, 8, 11, -1, 6],10),
    ([4,6],10)
    ]

for testCase in testCase:
        arr1 = testCase[0]
        targetsum = testCase[1]
        result = twoNumberSum(arr1,targetsum)
        if(result):
            print(f"ans pair:{result}")
        else:
            print("not found")

# total Time =O(n^2)
