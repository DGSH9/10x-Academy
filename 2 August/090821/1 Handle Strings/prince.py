n = int(input())
for _ in range(n):
    st = input().strip()
    l = len(st)
    if(l % 3 != 0 and l % 5 != 0):
        print('-', end='')
    if(l % 3 == 0):
        print("foo", end='')
    if(l % 5 == 0):
        print("bar", end='')
    print()
