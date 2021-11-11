def check(num):
    if(num == 1 or num == 0):
        return 'Yes'
    if(num % 10 == 0 or num % 20 == 0):
        return check(num//20) or check(num//10)
    else:
        return 'No'

t = int(input())
for i in range(t):
    num = int(input())
    print(check(num))
