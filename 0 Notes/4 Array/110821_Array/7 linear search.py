import array
a = array.array("i", [])
n = int(input())
for i in range(0,n):
    x= int(input())
    a.append(x)

flag = 0
index = 0
x=int(input("enter value to search"))
for i in range(0,len(a)):
    if(x==a[i]):
        flag = 1
        index = i
        break  
if(flag == 1):
    print("element found at index :",index)
else:
    print("element not found")