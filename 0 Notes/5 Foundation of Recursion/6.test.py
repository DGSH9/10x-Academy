def fun1(start, n):
    if(start == n):
        return
    else:
        print('hello')
        fun1(start+1, n)


fun1(1, 10)
