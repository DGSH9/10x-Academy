# https://6793fdf6.widgets.sphere-engine.com/lp?hash=3Gks4BeXx0
n,k = map(int,input().split())
arr1 = list(map(int,input().split()))

dict1 = {}
sum1 = 0
temp1 =  0

for i in range(len(arr1)):
    sum1+=arr1[i]
    if sum1 == k:
        temp1 = i+1
    elif(sum1-k) in dict1:
        temp1 = max(temp1,i-dict1[sum1-k])
    if sum1 not in dict1:
        dict1[sum1] = i
print(temp1)