# https://6793fdf6.widgets.sphere-engine.com/lp?hash=G4FLL1GsVo
# Hints==> only paint continuous sections of boards ==>Hints for modified binary search function

# mid will denote = how many boards each painter is painting

def valid(k,n,arr1,mid):
    count_painter = 1
    sum1 = 0
    for i in range(n):
        sum1 +=arr1[i]
        if sum1 >  mid:
            count_painter+=1
            sum1 = arr1[i]
        if count_painter > k:
            return False
    return True

def minTime(k, n, boards):
    start = min(boards)
    end = sum(boards)  # bcoz one painter can paint all the boards

    ans = -1
    while(start<=end):
        mid = (start+end)//2
        if valid(k,n,boards,mid) == True:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans
    
for _ in range(int(input())):
    k,n = [int(x)for x in input().split()]  # k -> painters  and n ->boards
    boards = [int(x)for x in input().split()]
    print(minTime(k, n, boards))
