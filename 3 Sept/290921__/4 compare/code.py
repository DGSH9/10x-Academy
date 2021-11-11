N,Q = map(int,input().split())
A = input()
B = input()

arr1A = list(A)
arr1B = list(B)
ans1 = set()
for i in range(Q):
    x = int(input())
    # for j in arr1B:
    for i in range(x):
        if arr1B[i]=='0':
            ans1.add('1')
        else:
            ans1.add(arr1B[i])
        
print(ans1)

