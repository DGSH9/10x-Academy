import array
a = array.array("i", [])
n = int(input())
for i in range(0, n):
    x = int(input())
    a.append(x)

max_arr = []
for i in range(0, len(a)-1):
    x = a[i]*a[i+1]
    max_arr.append(x)
print(max(max_arr))
