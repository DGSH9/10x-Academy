state = -1     # -1(off) ----> 1(on)
count = 0

n = int(input())
for i in range(n):
    ins = input()  # ins =instructions

    if(ins == 'Toggle'):
        if state == -1:
            count += 1
        state *= (-1)
    elif(ins == 'ON'):
        if state == -1:
            count += 1
        state = 1
    else:
        state = -1
print(count)


# Dry run
# | BEFORE | INSTRUCTION | RESULT |
# ------------------------------------
# | -1        | TOGGLE           | 1 |
# | 1         | TOGGLE           |-1|
# | -1        | OFF              | -1 |
# | -1        | TOGGLE           | 1 |
# | 1         | ON               | 1 |
