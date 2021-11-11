
P = int(input())    # --> this will take c1 constant time
T = int(input())    # --> this will take c2 constant time
R = int(input())    # --> this will take c3 constant time

SI = (P*T*R)//100   # --> this will take c4 constant time
print(SI)


# c1 + c2 +c3 + c4 = O(1) is the Time Complexity
