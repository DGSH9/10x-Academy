
def func(a):
    # a is passed as argument
    def func1(b):
        print(a, b, a+b)
    return (func1)


x = func(2)  # print(2,b,2+b)
y = func(3)  # print(3,b,3+b)

# x and y are functions
x(10)  # it can be a and b
y(20)  # it can be a and b

# print(type(x))      #----> here x is a function used as a function
