sentance = input()
words = sentance.split()  # ["DGSH","ghnjdkg"]

if (len(words) == 0):
    print(0)
else:
    n = len(words)
    print(len(words[n-1]))
