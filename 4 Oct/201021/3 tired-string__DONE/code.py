# https://6793fdf6.widgets.sphere-engine.com/lp?hash=2sbiSeQ8jD

st = input()

sum1 = 0
for i in st:
    sum1+=ord(i)

if sum1%2!=0:
    print('Yes')
else:
    print('No') 