t = int(input())
for i in range(t):
    a, s = map(int, input().split())
    if((s < 0) or (s > a)):
        print("Invalid")
    else:
        if((s % 8 == 1) or (s % 8 == 4)):
            print("L")
        elif((s % 8 == 2) or (s % 8 == 5)):
            print("M")
        elif((s % 8 == 3) or (s % 8 == 6)):
            print("U")
        elif(s % 8 == 7):
            print("SL")
        else:
            print("SU")
