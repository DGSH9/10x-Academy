n=int(input())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
x=int(input()) 
count=0
for i in arr:
    if i==x:
        count+=1
print(count)    