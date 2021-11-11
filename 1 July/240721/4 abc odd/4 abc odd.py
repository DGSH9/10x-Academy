# your code goes here
a, b = map(int, input().split())
third = 3-(a+b)
if((a*b*third) % 2 == 0):
    print("No")
else:
    print("Yes")
