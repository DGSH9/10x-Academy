n=int(input())
given_list=[]
for i in range(n):
    value_list=int(input())
    given_list.append(value_list)

min_value=given_list[0]
for i in range(1,n-1):
    if((given_list[i]+min_value) < 100):
            print("False")
            break
    else:
        print("True")
        break