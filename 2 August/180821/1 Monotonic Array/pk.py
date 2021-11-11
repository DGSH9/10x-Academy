n = int(input())
arr1 = []
for i in range(n):
    arr1.append(int(input()))
m = len(arr1)
a = 0
b = 0
for i in range(m-1):
    if(arr1[i] <= arr1[i+1]):
        a += 1
    elif(arr1[i] >= arr1[i+1]):
        b += 1
if(m-1 == (a or b)):
    print("True")
else:
    print("False")
