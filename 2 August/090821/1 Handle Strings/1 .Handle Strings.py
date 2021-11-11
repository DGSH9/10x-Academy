n = int(input())
for _ in range(n):
    st = input().strip()
    l = len(st)
    ans = ""
    if(l % 3 == 0):
        ans = ans+"foo"
    if(l % 5 == 0):
        ans = ans+"bar"
    elif(len(ans) == 0):
        ans = "-"
    print(ans)
