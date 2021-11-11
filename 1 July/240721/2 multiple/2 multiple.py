# your code goes here
givenNumber = int(input())
userInput = givenNumber
while(givenNumber > 0):
    if((givenNumber % 2 == 0) & (givenNumber % userInput == 0)):
        print(givenNumber)
        break
    else:
        givenNumber = givenNumber+1
