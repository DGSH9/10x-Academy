# https://6793fdf6.widgets.sphere-engine.com/lp?hash=qPsvnwWqob
def addSUbtract(arr1,i,k):
    #base case
    if (k ==0 and i ==len(arr1)):
        return 1
    if(i>=len(arr1)):
        return 0
    
    # main case
    return (addSUbtract(arr1,i+1,k) + addSUbtract(arr1,i+1,k-arr1[i]) + addSUbtract(arr1,i+1,k+arr1[i]))

k = int(input())
n = int(input())
arr1 = list(map(int,input().split()))
print(addSUbtract(arr1,0,k))