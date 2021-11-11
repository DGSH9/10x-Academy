n = int(input())
l = [-1]

for i in range(n):
    l.append(int(input()))
i = int(input())
k = i
sum = 0
while(i <= n):
    sum += l[i]
    i = i+k
print(sum)