# https://6793fdf6.widgets.sphere-engine.com/lp?hash=GuulSuvstL

sz = int(input())
if sz==1:
    print(0)
elif sz==2:
    print(1)
elif sz ==3:
    print(1)
elif sz ==4:
    print(2)

v1 = 0
v2 = 1
v3 = 1
for i in range(sz-4):
    next1 = v1+v2+v3
    v1 = v2
    v2 = v3
    v3 = next1

print(v1+v2+v3)