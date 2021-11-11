r = int(input("row :"))
c = int(input("column :"))

a = [0 for i in range(0,c) for j in range(0,r)]
b=[]

print(a)
print(b)
for i in range(r):
    b = []
    for j in range(0,c):
        x = int(input("enter element"))
        b.append(x)
    a[i] = b
print(a)