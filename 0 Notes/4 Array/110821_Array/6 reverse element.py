# input:  1 2 3 4
# output: 4 3 2 1
import array
a = array.array("i", [1, 2, 3, 4])
start = 0
end = len(a)-1

for i in range(int(len(a)/2)):
    temp = a[start+i]
    a[start+i] = a[end-i]
    a[end-i] = temp

print(a)
