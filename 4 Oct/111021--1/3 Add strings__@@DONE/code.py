# https://6793fdf6.widgets.sphere-engine.com/lp?hash=8AcZv6uoQ2

def addStrings(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]
    ans = ""
    # l1 = len(num1)
    # l2 = len(num2)

    if len(num2) > len(num1):
        num1,num2 = num2,num1
    
    cary = 0
    for i in range(len(num2)):
        temp = int(num1[i]) + int(num2[i]) + cary
        ans +=str(temp%10)
        cary = temp//10
    
    for i in range(len(num2),len(num1)):
        temp = int(num1[i]) + cary
        ans += str(temp % 10)
        cary = temp//10
    
    if cary !=0:
        ans+=str(cary)
    
    return ans[::-1]

    ### Here num1 & num2 are strings [Return the addition of these two strings as string]


## Do not change anything below this line:

for _ in range(int(input())):
    n1, n2 = input().split()
    print(addStrings(n1,n2))