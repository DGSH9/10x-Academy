# https://6793fdf6.widgets.sphere-engine.com/lp?hash=RARfDkFtQM
def find_k(l, k):
    l = 0
    h = len(l)-1
    while(l<=h):
        m = (l + h)//2
        if l[m]==k:
            return 'YES'
        elif(l[m]<k):
            l = m+1
        else:
            h = m-1
    return 'NO'
    
from sys import stdin
N,Q = input().split()
a = list(map(int,input().split(' ')))
a.sort() 
for i in range(int(Q)):
    k = int(input())
    print(find_k(a, k))