def twoNumberSum(arr1,targetsum):
    for i in range(len(arr1)):
        firstNum = arr1[0]
        for j in range(i+1,len(arr1)):
            secondNum = arr1[j]
            if(firstNum+secondNum==targetsum):
                return [firstNum,secondNum]
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
