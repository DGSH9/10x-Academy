# https://6793fdf6.widgets.sphere-engine.com/lp?hash=K5kufyFAGV
from collections import defaultdict
#a,b,c,d...... = consider keyboard as a linear set of keys


n = int(input())
dict1 = defaultdict(int)
#at which position,known character is there
A =[-1]*256                 # for storing character   #total 256 character and -1 means original position
#which character is there ,at a known original position



for i in range(n):
    a,b = input().lower().split()
    ord_a,ord_b = ord(a),ord(b)

    actual_position_a = ord_a if dict1[ord_a] ==0 else dict1[ord_a]
    actual_position_b = ord_b if dict1[ord_b] ==0 else dict1[ord_b]

    A[actual_position_b]  = ord_a
    A[actual_position_a]  = ord_b

    dict1[ord_b],dict1[ord_a] = actual_position_a,actual_position_b

command  = list(input())
for i in range(len(command)):
    # ordd = ord(command[i])
    if command[i].isupper():
        if A[ord(command[i].lower())] != -1:
            command[i] = chr(A[ord(command[i].lower())])
        command[i] = command[i].upper()
    else:
        if A[ord(command[i].lower())] !=-1:
            command[i] = chr(A[ord(command[i].lower())])
    
print("".join(command))




















#my own method


# n = int(input())
# for i in range(n):
#     a,b = map(str,input().split())
    
#     st = input()

#     arr1 =list(st)
#     # print(arr1)
#     i1 = 0
#     i2 = 0
#     for i in range(len(arr1)):
#         if arr1[i] == a:
#             i1 = i
#         if arr1[i]== b:
#             i2 = i
#     # for i in range(n):
#     if arr1[i1].isupper() and arr1[i2].isupper():
#         arr1[i1],arr1[i2] = arr1[i2],arr1[i1]
#     elif arr1[i1].isupper() and arr1[i2].islower():
#         arr1[i1].lower() and arr1[i2].upper()
#         arr1[i1],arr1[i2] = arr1[i2],arr1[i1]

#     elif arr1[i1].islower() and arr1[i2].isupper():
#         arr1[i1].upper() and arr1[i2].lower()
#         arr1[i1],arr1[i2] = arr1[i2],arr1[i1]
#     else:
#         arr1[i1],arr1[i2] = arr1[i2],arr1[i1]

#     for i in arr1:
#         print(i,end="")