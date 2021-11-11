def func2():
    print("hello world")
    global a, b

    a = 2
    b = 3
    print(a, b)


func2()
print(a, b)
