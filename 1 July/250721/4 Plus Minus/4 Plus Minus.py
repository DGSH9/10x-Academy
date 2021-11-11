givenNum = int(input())
temp=0
for i in range(givenNum):
    x = int(input())
    if(i % 2 ==0):
        temp+=x
    else:
        temp-=x
print(temp)