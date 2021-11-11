# your code goes here
givenNum = int(input())
temp=0
count = 1
for i in range(givenNum):
    x = int(input())
    if(i == 0):
        temp=x
    else:
        if(x==temp):
            count+=1
print(count)