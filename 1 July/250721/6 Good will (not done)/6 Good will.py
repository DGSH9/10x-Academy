
n = int(input())               
for i in range(n):
    for j in range(1,(n+1-i)):
        print(" ",end="")
    for j in range(i*2+1):
      if((i+j)%2==0):
        print("*",end="")
      else:
        print("$",end="")
    print() 