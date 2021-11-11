def find_k(l, k):               # k = 50
    first = 0                   #0
    last = len(l)-1             #4
    while(first<=last):          # 0<4(true)  => 3<4
        mid = (first+last)//2   # m = 2      => (3+4)//2 = 3
        if l[mid]==k:           #l[2] == 50  => No
            return 'YES'
        elif(k<l[mid]):         #50 < 40(No)
            last = mid-1         
        elif(k>l[mid]):         #50 > 30 => 
            first=mid+1        # f = 3  =>f = 4
    return "NO"

"""
50 40 30 20 10
10 20 30 40 50

==> 20

"""

    # Implement this and return YES if found else return No
    
from sys import stdin
N,Q = input().split()
a = list(map(int,input().split(' ')))
a.sort() 
for i in range(int(Q)):
    k = int(input())
    print(find_k(a, k))