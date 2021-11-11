n = int(input())
fact = 1
if(n < 0):
    print('undefined')
else:
    for i in range(n, 0, -1):
        fact = fact*i
    print(fact)
