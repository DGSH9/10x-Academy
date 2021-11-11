#[1,2,3,4,5]
#sum = 6

import array
a = array.array("i",[1,2,3,4,5])
sum = 0
for i in range(len(a)):
    if(a[i]%2==0):
        sum+=a[i]
print(sum)