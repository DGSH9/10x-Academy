st = input()
mx = 0
for i in range(1,len(st)+1):
    for j in range(len(st)-i+1):
        tmp = set(st[j:j+i])
        if(len(tmp)==1):
            mx = max(mx,len(st[j:j+i]))
print(mx)