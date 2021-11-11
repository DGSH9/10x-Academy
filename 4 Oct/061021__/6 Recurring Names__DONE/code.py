# https://6793fdf6.widgets.sphere-engine.com/lp?hash=X6UzEPUlNs

k = int(input())
d = {}
names = input().split()

for i in names:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
# print(d)

arr1 = []
for i in d:
    # print(d[i])
    if d[i] > k:
        arr1.append(i)
# print(arr1)
arr1.sort()
if len(arr1) == 0:
    print('no such names in this town!!!')
[print(i) for i in arr1]
