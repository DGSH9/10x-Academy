
l = int(input())        # --> this will take c1 constant time
b = int(input())        # --> this will take c2 constant time

if(l > 0 and b > 0):
    print(int(l*b))   # --> this will take c3 constant time
else:
    print(0)          # --> this will take c4 constant time

# c1 + c2 + c3 + c4  = O(1) is the time Complexity
