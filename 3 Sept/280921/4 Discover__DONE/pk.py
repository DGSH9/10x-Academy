def find_k(arr, k):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==k):
            return "YES"
        elif(arr[mid]<k):
            low=mid+1
        else:
            high=mid-1
    return "NO"    

from sys import flags, stdin
N,Q = input().split()
a = list(map(int,input().split(' ')))
a.sort() 
for i in range(int(Q)):
    k = int(input())
    print(find_k(a, k))