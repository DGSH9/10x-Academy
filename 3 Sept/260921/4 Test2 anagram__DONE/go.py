for i in range(int(input())):
    st1, st2 = map(str,input().split())
    st1Empty = ''.join(sorted(st1))
    st2Empty = ''.join(sorted(st2))
    if st1Empty == st2Empty:
        print(True)
    else:
        print(False)