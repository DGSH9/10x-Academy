givenNumber = int(input())
reqNumber = givenNumber
if(givenNumber > 0):
    givenNumber = givenNumber
else:
    givenNumber = givenNumber*(-1)
sumDigit = 0
while(givenNumber > 0):
    lastDigit = givenNumber % 10
    sumDigit = sumDigit*10+lastDigit
    givenNumber = givenNumber//10
if(reqNumber > 0):
    print(sumDigit)
else:
    print(sumDigit*(-1))