
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = map(int,input().split())
str = input()
ans = sorted(str)
tall_string = ans[len(ans)-1]
if(tall_string=='a' or'A'):
    tall_value = a

if(tall_string=='b'or'B'):
    tall_value = b

if(tall_string=='c'or'C'):
    tall_value = c

if(tall_string=='d'or'D'):
    tall_value = d

if(tall_string=='e'or'E'):
    tall_value = e

if(tall_string=='f'or'F'):
    tall_value = f

if(tall_string=='g'or'G'):
    tall_value = g

if(tall_string=='h'or'H'):
    tall_value = h

if(tall_string=='i'or'I'):
    tall_value = i

if(tall_string=='j'or'J'):
    tall_value = j

if(tall_string=='k'or'K'):
    tall_value = k

if(tall_string=='l'or'L'):
    tall_value = l

if(tall_string=='m'or'M'):
    tall_value = m

if(tall_string=='n'or'N'):
    tall_value = n

if(tall_string=='o'or'O'):
    tall_value = o

if(tall_string=='p'or'P'):
    tall_value = p

if(tall_string=='q'or'Q'):
    tall_value = q

if(tall_string=='r'or'R'):
    tall_value = r

if(tall_string=='s'or'S'):
    tall_value = s

if(tall_string=='t'or'T'):
    tall_value = t

if(tall_string=='u'or'U'):
    tall_value = u

if(tall_string=='v'or'V'):
    tall_value = v

if(tall_string=='w'or'W'):
    tall_value = w

if(tall_string=='x'or'X'):
    tall_value = x

if(tall_string=='y'or'Y'):
    tall_value = y

if(tall_string=='z'or'Z'):
    tall_value = z


length = len(str)
width1 = 1
print(length*tall_value)
