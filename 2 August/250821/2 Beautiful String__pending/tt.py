from collections import defaultdict
def Beautiful(st):
    counta,countb,countc = 0,0,0
    d = defaultdict(int)
    d[(0,0)] =1
    res =  0

    for i in st:
        if i=='a':
            counta +=1
        elif(i=='b'):
            countb+=1
        elif(i=='c'):
            countc+=1
        
        z = (counta-countb,counta-countc)

        res +=d[z]
        d[z] +=1

    return res

for i in range(int(input())):
    print(Beautiful(input()))