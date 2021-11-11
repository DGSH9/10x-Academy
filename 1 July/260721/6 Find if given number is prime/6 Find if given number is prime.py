t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for j in range(1,n+1):
        if(n % j == 0):
            count += 1
    if(count == 2):
        print("Yes")
    else:
        print("No")