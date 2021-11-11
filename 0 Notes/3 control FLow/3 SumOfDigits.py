# givenNum = int(input())
# sumOfDigits = 0
# lastDigit = givenNum % 10
# sumOfDigits = sumOfDigits + lastDigit
# givenNum = givenNum // 10


# lastDigit = givenNum % 10
# sumOfDigits = sumOfDigits + lastDigit
# givenNum = givenNum // 10

# lastDigit = givenNum % 10
# sumOfDigits = sumOfDigits + lastDigit
# givenNum = givenNum // 10

# solution 1
givenNum = int(input())
sumOfDigits = 0
while(givenNum>0):
    lastDigit = givenNum % 10
    sumOfDigits = sumOfDigits + lastDigit
    givenNum = givenNum // 10
print(sumOfDigits)



# solution 2
givenNum = int(input())
sumOfDigits = 0
while(givenNum > 10):
    lastDigit = givenNum % 10
    sumOfDigits = sumOfDigits + lastDigit
    givenNum = givenNum // 10
sumOfDigits = sumOfDigits + givenNum
print(sumOfDigits)