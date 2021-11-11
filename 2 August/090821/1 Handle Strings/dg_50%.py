n = int(input())
for i in range(n):
    x = input()
    len1 = len(x)
    if(len1 % 3 == 0):
        print("foo")
    elif(len1 % 5 == 0):
        print("bar")
    elif(len1 % 3 == 0 and len1 % 5 == 0):
        print("foobar")
    else:
        print("-")
