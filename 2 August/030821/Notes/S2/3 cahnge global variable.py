def func2():
    print("hello world")
    global a    # have access to global variable
    global b    # have access to global variable

    a += 2
    b += 3
    print(a, b)


a = 0
b = 0
func2()
print(a, b)
