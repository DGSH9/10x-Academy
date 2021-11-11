# https://6793fdf6.widgets.sphere-engine.com/lp?hash=PMYTaB6etG
for _ in range(int(input())):
    st = input()
    punct = """!@#$%^&*()-_=+`~;:'" /?.>,<[{]}\|"""
    ans = ""
    for i in st:
        if i not in punct:
            ans+=i
    ans = ans.lower()
    ans_reversed ="".join(reversed(ans))
    if ans == ans_reversed:
        print(True)
    else:
        print(False)