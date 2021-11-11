import array
a = array.array("i",[2,1,3,4,5])
max = 0
min = a[0]
for i in range(len(a)):
    if(a[i]>max):
        max=a[i]
    if(a[i]<min):
        min = a[i]
print("maximum value is :",max)
print("minimum value is :",min)