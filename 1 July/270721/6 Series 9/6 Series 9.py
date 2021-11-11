givenNum=int(input())
sum1=0
pp=9
for i in range(1,givenNum+1):
    sum1 = sum1+ pp
    pp=(pp*10)+9
print(sum1)