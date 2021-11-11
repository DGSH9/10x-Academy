s = input()
s_blank = ""
for i in s:
    if i.isupper():
        s_blank+=i.lower()
    else:
        s_blank+=i.upper()
print(s_blank)