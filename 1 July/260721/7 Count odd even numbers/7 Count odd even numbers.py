n=int(input())
Even_count=0
Odd_count=0
for i in range(1,n+1):
    x=int(input())    

    if(x%2==0):
        Even_count+=1
    else:
        Odd_count+=1
print(Odd_count)
print(Even_count)