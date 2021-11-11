# nth fibb number =>   nth = (n-1)th + (n-2)th
#                      f(n) = f(n-1) + f(n-2)

def feb(n):
    if(n==0):
        return 'invalid'
    if(n==1):
        return 0
    if(n==2):
        return 1
    x = feb(n-1)
    y = feb(n-2)
    return x+y

print(feb(10))