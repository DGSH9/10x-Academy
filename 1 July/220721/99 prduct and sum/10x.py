givenNumber = int(input())
sumDigits = 0
productDigit = 1
if(givenNumber == 0):
    print(0)
else:
    while givenNumber > 0:
        lastDigit = givenNumber % 10
        sumDigits = sumDigits+lastDigit
        productDigit = productDigit*lastDigit
        givenNumber = givenNumber//10
    print(productDigit-sumDigits)
