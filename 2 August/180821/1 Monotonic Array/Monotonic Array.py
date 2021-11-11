n = int(input())
arr = []
brr = []
for i in range(n):
	arr.append(int(input()))
for i in range(n):
	brr.append(int(input()))
ans = []
for i in range(n):
	ans.insert(brr[i],arr[i])
for i in ans:
	print(i)
