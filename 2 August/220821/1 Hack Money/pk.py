def check(start, end):
    if(start == end):
        return "Yes"
    if(start < end):
        a = check(start*10, end)
        b = check(start*20, end)
        if(a == 'Yes' or b == 'Yes'):
            return "Yes"
        else:
            return "No"


t = int(input())
for i in range(t):
    num = int(input())
    print(check(1, num))
