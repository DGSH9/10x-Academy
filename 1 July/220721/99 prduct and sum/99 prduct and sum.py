givenNumber = int(input())
temp = givenNumber
sumDigit = 0
productDigit = 1
while(temp > 0):
    d = temp % 10
    temp //= 10
    sumDigit += d
    productDigit *= d
print(productDigit-sumDigit)

# ---------------------------------------------
givenNumber = int(input())
sumDigits = 0
productDigit = 1

while givenNumber > 0:
    lastDigit = givenNumber % 10
    sumDigits = sumDigits+lastDigit
    productDigit = productDigit*lastDigit
    givenNumber = givenNumber//10
print(productDigit-sumDigits)
