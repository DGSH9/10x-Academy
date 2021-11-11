n = int(input())
t = int(input())
cost = [0]*t
tb = []
for i in range(n):
	x = int(input())
	tb.append(x)
for i in range(n):
	x = int(input())
	cost[tb[i]-1]+=x
mx = max(cost)
for i in range(t):
	if(cost[i]==mx):
		print(i+1)
