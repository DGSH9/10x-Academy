import array
a = array.array("i", [1, 2, 3, 4, 5])
print(a, "type = ", type(a))

print(a[0])
print(a[2])
print(a[1:])
print(a[1:3])
print(a[:3])

for i in range(len(a)):
    print(a[i])

print(" ")

for i in range(len(a)-1, -1, -1):
    print(a[i])


# for i in range(len(a)):
#     print(a[i])
