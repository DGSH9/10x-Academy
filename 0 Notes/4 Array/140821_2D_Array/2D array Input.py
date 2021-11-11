###############################
n = int(input())
arr = list(map(int, input().strip().split()))[:n]

################################
h = int(input())
lst = []
for val in range(0, h):
    lst.append([int(i) for i in input().split(' ')])
