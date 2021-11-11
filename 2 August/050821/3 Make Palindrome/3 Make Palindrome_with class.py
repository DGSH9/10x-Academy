class P:
    def __init__(self, st):
        self.st = st

    def getSt(self):
        return self.st

    def setPl(self, n):
        if len(self.st) > 1:
            if n == 0:
                self.st = self.st+self.st[::-1]
            else:
                self.st = self.st+self.st[::-1][1:]
        else:
            self.st = self.st


str = input()
n = int(input())
p = P(str)
print(p.getSt())
p.setPl(n)
print(p.getSt())
