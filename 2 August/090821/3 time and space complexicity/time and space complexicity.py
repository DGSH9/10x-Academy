# Forming names

n = int(input())  # 1, 1
st = input()  # 1, 1
at = input()  # 1, 1
x = "true"
for i in st:  # n, 0     (time and space for this loop)
    if i not in at:
        x = "false"
        break
print(x)  # 1, 1

# total time  = O(n)
# total space = O(1)
