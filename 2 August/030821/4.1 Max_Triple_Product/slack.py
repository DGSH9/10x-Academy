n = int(input())
list1 = []
for i in range(n):
    list1.append(int(input()))
list1.sort()
print(list1[-1]*list1[-2]*list1[-3])
