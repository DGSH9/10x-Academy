# print principle diagonal of 2d array
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]

# output = 1,5,9

r = int(input("row :"))
c = int(input("column :"))

a = [[0 for i in range(0, c)] for j in range(0, r)]
b = []
for i in range(r):
    b = []
    for j in range(0, c):
        x = int(input("enter element"))
        b.append(x)
    a[i] = b
print(a)
print(a[0][0], a[1][1], a[2][2])
