# Functions



def sum_of_numbers(list_of_numbers):
    sumation = 0
    for number in list_of_numbers:
        # print('Number are : ',number)
        sumation = sumation+ number
    # print('Sum',sumation)
    return sumation

num1 = [1,2,3,4,5,6]
sum_numbers1 = sum_of_numbers(num1)
print(sum_numbers1)

num2 = [1,2,3,4,5,6,8,9,56,564,3,2111]
sum_numbers2 = sum_of_numbers(num2)
print(sum_numbers2)


# if sum_of_numbers % 2 ==0:
#     print('SUm is even')
# else:
#     print('Sum is odd')