s = input()                         #1, 1
a = 0                               #1, 1
e = 0                               #1, 1
i = 0                               #1, 1
o = 0                               
u = 0                               
s_len = len(s)                      #n, 1
for j in range(s_len):              #n, 1   =>(time and space for this loop)
    if(s[j] == 'a'):                
        a += 1
    elif(s[j] == 'e'):
        e += 1
    elif(s[j] == 'i'):
        i += 1
    elif(s[j] == 'o'):
        o += 1
    elif(s[j] == 'u'):
        u += 1
print("occurence of a is", a)       #1, 0   =>(time and space)
print("occurence of e is", e)
print("occurence of i is", i)
print("occurence of o is", o)
print("occurence of u is", u)

# time = O(n) + O(n) = O(2*n) => O(n)
# space = O(1)                => O(n)