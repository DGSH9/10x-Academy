# Given an inetegr print the multiplacation table of that integer
# input    --> an integer
# output   --> multiplication table

# example are
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# .........
# 2 x 10 = 20

givenNum = int(input())
multiplier =1
while(multiplier<=10):
    print(str(givenNum) + " x " + str(multiplier) + "=" + str(givenNum * multiplier))
    multiplier = multiplier + 1

# print(str(givenNum) + " x <multiplier> = " + str(givenNum * <multiplier>))

# print(str(givenNum) + " x 1 = " + str(givenNum*1))
# print(str(givenNum) + " x 2 = " + str(givenNum*2))
# print(str(givenNum) + " x 3 = " + str(givenNum*3))
# print(str(givenNum) + " x 4 = " + str(givenNum*4))
# print(str(givenNum) + " x 5 = " + str(givenNum*5))
# print(str(givenNum) + " x 6 = " + str(givenNum*6))
# print(str(givenNum) + " x 7 = " + str(givenNum*7))
# print(str(givenNum) + " x 8 = " + str(givenNum*8))
# print(str(givenNum) + " x 9 = " + str(givenNum*9))
# print(str(givenNum) + " x 10= " + str(givenNum*10))
