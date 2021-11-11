def sumOfFirstN(n):
    # Implement this function
    # 1.Base case
    if(n == 1):
        print(1, 1)
        return 1
    # 2.Normal Case
    else:
        ans = n + sumOfFirstN(n-1)  # 5+4+3+2+1
        print(n, ans)
        return ans
# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    sumOfFirstN(n)
