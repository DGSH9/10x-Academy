n = int(input())
for i in range(1, n+1):
    for k in range(1, n+1-i):
        print(" ", end="")
    for j in range(1, i+1):
        print("#", end="")
    print("\n")


# https://6793fdf6.widgets.sphere-engine.com/lp?hash=ZPQZVWDzZu