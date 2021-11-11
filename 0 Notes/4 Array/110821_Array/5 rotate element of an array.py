# rotate element of array
# input : 1 2 3 4
# output: 4 1 2 3

######## First method using inbuilt functio ############
# a = [1,2,3,4]
# a.remove(4)
# a.insert(0,4)
# print(a)


######## Second Method ###############################
# import array
# a=array.array("i",[1,2,3,4])
# temp = a[0]
# for i in range(1,len(a)):
#     temp1=a[i]
#     a[i]=temp
#     temp=temp1
# a[0] =  temp
# print(a)

######## User input #################################
import array

a = array.array("i",[])
n=int(input())
for i in range(0,n):
    x=int(input())
    a.append(x)

temp = a[0]
for i in range(1,len(a)):
    temp1=a[i]
    a[i]=temp
    temp=temp1
a[0] =  temp
print(a)