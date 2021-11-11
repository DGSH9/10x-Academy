import array

a = array.array("i", [])

n = int(input("enter length of array"))

for i in range(0, n):
    temp = int(input("enter elements :"))
    a.append(temp)

print(a)


###############################
n = int(input())
arr = list(map(int, input().strip().split()))[:n]

################################
h = int(input())
lst = []
for val in range(0, h):
    lst.append([int(i) for i in input().split(' ')])
