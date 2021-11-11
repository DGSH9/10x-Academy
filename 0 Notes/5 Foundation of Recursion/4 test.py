def fun1(m):
    m = m+1
    print(m)

def fun2(x):
    x = x+1
    print(x)
    fun1(x)

m = 10
print(m)
fun2(m)
