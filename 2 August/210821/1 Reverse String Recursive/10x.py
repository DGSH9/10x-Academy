def reverse(s):
    # base case
    if s == "":
        return ""
    # normal case
    return s[-1] + reverse(s[:-1])   # o + (lleh) =>o+(l+(leh)) + o+(l+(l+(eh))) + o+(l+(l+(e+(h))))

t = int(input())
for i in range(t):
    s=input()
    print(reverse(s))

