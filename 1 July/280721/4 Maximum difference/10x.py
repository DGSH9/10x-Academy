n = int(input())
l = list(map(int, input().split()))
maxi = l[0]
mini = l[0]
for i in l:
    maxi = max(l, i)
    mini = min(l, i)
print(maxi - mini)