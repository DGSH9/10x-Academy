st = input()
arr = list(map(str,input().split()))
ans=0
for t in arr:
	count=0
	for i in t:
		if i in st:
			count+=1
	if count==len(t):
		ans=max(ans,count)
print(ans)