# https://6793fdf6.widgets.sphere-engine.com/lp?hash=Inr1z9fqMj

a = int(input())
b = int(input())
quotient  = a//b 
remainder = a%b
print(quotient)
print(remainder)
text = ', '.join(str(x) for x in [quotient,remainder])
print("({0})".format(text))
