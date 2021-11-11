
str = input()
n = int(input())
ans = ""
if len(str)>1:
    if n==0:
        ans=str+str[::-1]
    else:
        ans=str+str[::-1][1:]
else:
    ans=str
print(ans)