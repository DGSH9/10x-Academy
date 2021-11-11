st = input().split()
arr = []
mx = 0
idd=-1
for i in range(len(st)):
	arr.append(len(st[i]))
	if(mx<arr[i]):
		mx = arr[i]
		idd=i
if(idd==-1):
	print(0)
else:
	print(mx)