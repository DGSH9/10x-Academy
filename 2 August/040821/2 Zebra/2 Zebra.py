n = int(input())
arr1 = []
for i in range(n):
    x = int(input())
    arr1.append(x)

white = 0
black = 0
for i in arr1:
    if(i > 0):
        white += 1
    else:
        black += 1
if(white == black):
    print(True)
else:
    print(False)
