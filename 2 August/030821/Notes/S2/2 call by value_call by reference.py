def func2():
    print("hello world")
    a = 2
    b = 3
    print(a, b)


# here this is a global variable
a = 0
b = 0
func2()  # calling local variable
print(a, b)  # calling global variable
