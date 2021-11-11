# Square matrix(if row equal to column  ) and rectangle matrix(if row  not equal to column)
# Square(r==c) and Rectangle(r!=c)

r = [[1,7,3],[4,5,6],[7,8,9]]
c = [[1,1,1,2],[6,11,12,2],[4,21,22,12]]

result = [[0 for i in range(4)] for j in range(3)]

for i in range(len(r)):
    for j in range(len(c)):
        print(j)