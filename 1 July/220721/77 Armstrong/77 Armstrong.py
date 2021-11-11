number = int(input())
summ = 0
temp = number
while(temp >0):
    digit = temp % 10
    summ += digit**3
    temp = temp//10
if(number == summ):
    print("YES")
else:
    print("No")



# -----------------------------------
n = int(input())
a = int(n/100)
b = int((n-(a*100))/10)
c = int(n-(a*100+b*10))
summ = a**3+b**3+c**3
if(n == summ):
    print("YES")
else:
    print("No")

# ----------------------------------best----------------
number = int(input())

reqNumber = number
sum = 0
while(number > 0):
    lastDigit = number % 10
    sum = sum+(lastDigit**3)
    number = number//10
if(reqNumber == sum):
    print("Yes")
else:
    print("No")

