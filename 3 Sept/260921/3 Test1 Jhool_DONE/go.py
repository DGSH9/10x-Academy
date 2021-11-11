for j in range(int(input())):
    st = input()
    rCount = 0
    uCount = 0
    bCount = 0
    yCount = 0
    for i in st:
        if i == 'r':
            rCount += 1
        elif(i == 'u'):
            uCount += 1
        elif(i == 'b'):
            bCount += 1
        elif(i == 'y'):
            yCount += 1
    print(min(rCount,uCount,bCount,yCount))

