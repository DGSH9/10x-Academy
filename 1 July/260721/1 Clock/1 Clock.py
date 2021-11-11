num1,num2=map(int,input().split())
sum=num1+num2
if(sum<=12):
    print(sum)
elif(sum % 12==0):
    print("12")
else:
    print(sum%12)