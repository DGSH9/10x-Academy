import math
for i in range(int(input())):
    r,g,b = map(int,input().split())
    var1 = min(r,min(g,b))
    r = r - var1
    g = g - var1
    b = b - var1
    # var1 += math.ceil(r/2) + math.ceil(g/2) + math.ceil(b/2)
    var1 += (r + g + b + 1)//2
    print(var1)