import array
a = array.array("i", [])
n = int(input())
for i in range(0, n):
    x = int(input())
    a.append(x)
mx = a[0]*a[1]
for i in range(0, len(a)-1):
    x = a[i]*a[i+1]
    mx = max(mx, x)
print(mx)
