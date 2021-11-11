# base case        => if(a%b) then return b
# recurse relation => gcd(a,b)    --> gcd(b,a%b)

def gcd(a, b):
    if(a % b == 0):
        return b
    else:
        return gcd(b, a % b)


print(gcd(30, 12))
