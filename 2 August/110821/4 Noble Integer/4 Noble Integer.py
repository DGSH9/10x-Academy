n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
flag = 0
for i in range(0, len(arr)):
    c = 0
    for j in range(0, len(arr)):
        if(arr[i] < arr[j]):
            c += 1
    if(c == arr[i]):
        flag = 1
if(flag == 1):
    print(1)
else:
    print(-1)
