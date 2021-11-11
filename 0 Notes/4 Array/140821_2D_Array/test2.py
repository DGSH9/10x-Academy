# print principle diagonal of 2d array
# [[1,2,3],      index = [[00,01,02],
#  [4,5,6],               [10,11,12],
#  [7,8,9]]               [20,21,22]]
# output = 1,5,9

r = int(input("row :"))
c = int(input("column :"))
a = [[0 for i in range(0, c)] for j in range(0, r)]
b = []

for i in range(len(a)):
    for j in range(len(a[i])):
        x = int(input("enter elements"))
        a[i][j] = x
print(a)
for i in range(r):
    for j in range(c):
        # print(a[i][j])   -->for this question
        if(i == j):
            print(a[i][j])
