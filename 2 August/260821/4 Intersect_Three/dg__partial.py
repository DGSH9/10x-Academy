n1 = int(input())
arr1 = []
for i in range(n1):
    arr1.append(int(input()))

n2 = int(input())
arr2 = []
for i in range(n2):
    arr2.append(int(input()))

n3 = int(input())
arr3 = []
for i in range(n3):
    arr3.append(int(input()))

arr4 = []
for i in range(len(arr1)):
    for j in range(len(arr2)):
        for k in range(len(arr3)):
            if(arr1[i] == arr2[j]):
                if(arr1[i] == arr3[k]):
                    arr4.append(arr1[i])
# for i in arr4:
#     print(arr4[i])
# print(arr4)
if len(arr4) > 0:
    for i in arr4:
        print(i)
else:
    print(-1)

# print(arr1)
# print(arr2)
# print(arr3)
