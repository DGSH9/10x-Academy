def isSubSequence(str1, str2):
    m = len(str1)
    n = len(str2)
    j = 0    # Index of str1
    i = 0    # Index of str2
    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j+1
        i = i + 1
    return j == m

st = input()
arr = list(map(str,input().split()))
ans=0
for t in arr:
    if(isSubSequence(t,st)):
        ans=max(ans,len(t))
print(ans)