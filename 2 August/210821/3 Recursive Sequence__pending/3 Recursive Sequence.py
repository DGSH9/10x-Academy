def seq(n):
    # base case
    if(n == 1):
        return 1
    term = 1
    start = ((n-1)*(n-1+1))//2 + 1
    end = start + n

    for i in range(start, end):
        term *= 1
    # main case
    return seq(n-1) + term


for i in range(int(input())):
    print(seq(int(input())))
