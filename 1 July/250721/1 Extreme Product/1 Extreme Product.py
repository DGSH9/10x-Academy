n=int(input())
arr=[]
mn=0
mx=0
for i in range(n):
    x=int(input())
    if i==0:
        mx=x
        mn=x
    if mx<x:
        mx=x
    if mn>x:
        mn=x
print(mx*mn)