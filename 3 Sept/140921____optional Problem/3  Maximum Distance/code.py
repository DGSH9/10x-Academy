# https://6793fdf6.widgets.sphere-engine.com/lp?hash=zgzjLGi6kT

n = int(input())
arr1 = list(map(int,input().split()))

first = []
second = []
for i in range(n):
    first.append((i-1)*arr1[i])
    second.append((i+1)*arr1[i])
print(max(first) - min(second))