n=int(input())
arr1 = list(map(int,input().split()))

#1 sort -> set -> len-2
#2 set -> list -> sort -> len-2
arr1 = list(set(arr1))
arr1.sort()
ans = arr1[:len(arr1)-2]

if len(ans) == 0:
    print(-1)
else:
    print(*ans)