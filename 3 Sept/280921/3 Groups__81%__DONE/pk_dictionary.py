for _ in range(int(input())):
    n = int(input())
    arr = input().split()

dict1 = {}
for st in arr:
    tmp=st
    st = list(st)
    st.sort()
    st=''.join(st)
    if st in dict1:
        dict1[st].append(tmp)
    else:
        dict1[st]=[tmp]

print(dict(sorted(dict1.items(), key=lambda item: item[1])))
print(max(dict1, key=dict1.get))

























"""
1
6
eat tea tan ate nat bat


tea

aet=[eat,tea]

{}

bat dfafas fdasirnF(int if)

"""