n = int(input())

while(n > 0):
    if(n % 2 == 0):
        n -= 11
    else:
        n -= 21
print(n)
