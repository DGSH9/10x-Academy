x = input()
res = 0
for i in x:
    res = res+int(i)**3
if(int(x) == res):
    print("Yes")
else:
    print("No")
