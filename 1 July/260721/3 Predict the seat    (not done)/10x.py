berths = ['L', 'M', 'U', 'L', 'M', 'U', 'SL', 'SU']
for i in range(int(input())):
    b, c = map(int, input().split())

    if(c > b):
        print("Invalid")
    else:
        c = c % 8
        if(c == 0):
            print('SU')
        else:
            print(berths[c-1])
