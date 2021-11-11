number1 = int(input())
number2 = int(input())
def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    print(a)
    print(b)
swap_numbers(number1, number2)