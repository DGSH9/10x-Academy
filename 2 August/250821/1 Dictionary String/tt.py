def longestMatch(st,d):
    for d1 in d:
        i=0
        for j in range(len(st)):
            if st[j]==d1[i]:
                i+=1
            if(i==len(d1)):
                return len(d1)
    return 0        
    
st = input()
d = input().split()

d.sort(key = lambda x:len(x),reverse=True)
print(longestMatch(st,d))