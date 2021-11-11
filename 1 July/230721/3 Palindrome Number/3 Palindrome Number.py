givenNumber = int(input())
reqNumber = givenNumber
sumDigit = 0
while(givenNumber > 0):
    lastDigit = givenNumber % 10
    sumDigit = sumDigit*10+lastDigit
    givenNumber = givenNumber//10
if(reqNumber == sumDigit):
    print(True)
else:
    print(False)