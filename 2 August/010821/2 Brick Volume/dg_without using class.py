n = int(input())
x, y = map(int, input().split())
length = 100
width = 60
height = 40
if(x == (-1)):
    count1 = int(int((length * width * y) * 0.00005) * n)
    print(count1)
else:
    count2 = int((length * width * height) * 0.00005 * n)
    print(count2)
