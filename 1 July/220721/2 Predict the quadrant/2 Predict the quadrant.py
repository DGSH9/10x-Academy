T = int(input())
t = 0
while(t < T):
    x, y = input().split()
    x = int(x)
    y = int(y)

    if(x > 0):
        if(y > 0):
            print("Q1")
        else:
            print("Q4")
    else:
        if(y > 0):
            print("Q2")
        else:
            print("Q3")
    t += 1
