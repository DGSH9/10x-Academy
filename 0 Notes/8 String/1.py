var = 'my name is durgesh'    #string is immutable
print(id(var))
var = var + 'f'
print(id(var),)

arr1 = ['abc'] #lsit is mutable
print(id(arr1))
arr1.append('fgh')
print(id(arr1))

# print(var[1:4:1])
print(var[1:10:2])

var1 = 'abc'
var2 = 'Abc'
if var1==var2:
    print(True)
else:
    print(False)

""" *****************COnvert character********************** """

# capitalize() and split()
var3 = 'my name is durgesh'
print(var3.capitalize())   #---------> First letter capitalize
print(var3.title())        #---------> First characrter of each word capitalize
print(var3.split(" "))     #---------> Return a list with separated from space
print(var3.split(","))

# strip()
var4 = "--India--"
print(var4.strip("--"))     #--------->that charactyer is present or not   used to remove
print(var4.rstrip("--"))    #--------->strip from right
print(var4.lstrip("--"))    #--------->strip from left
print(var4.strip(" "))  

# replace and find
var5 = "India is great and is great"
print(var5.replace("India","New India"))
print(var5.find("is"))      #--------->Find index
# print(var5.find("zz"))      
print(var5.rfind("is"))     #--------->find from right


# lower() and upper()
print(var5.lower())
print(var5.upper())

# isdigit(),isalpha()
var6 = "Indiais"
print(var6.isdigit())
print(var6.isalpha())
print(var6.isspace())
print(var6.replace("is",""))


arr2 = ["india","great"]
print("".join(arr2))

# add string with integer
var8 = "DGSH{}"
var8 = var8.format(9)
print(var8)

# concatinate string with integer
var7 = "My age is {},I live at {} square street"
var7 = var7.format(23,47)
print(var7)


# var9 = "India is "great" and my name is durgesh"   --->we cant declare like this
var9 = "India is \"great\" and my name is durgesh"
print(var9)
