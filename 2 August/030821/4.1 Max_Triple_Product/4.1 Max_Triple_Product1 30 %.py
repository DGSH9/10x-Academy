n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()
lst.remove(lst[0])
pro = 1
for i in range(len(lst)):
    pro = pro*lst[i]
print(pro)
