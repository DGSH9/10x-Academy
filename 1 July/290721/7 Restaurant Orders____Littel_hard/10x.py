order_num = int(input())
table_num = int(input())

# [0+100,0+200,0+300+200,0+500] = [100,200,500,500]
res = [0 for i in range(table_num)]

tableno = []
for i in range(order_num):
    tableno.append(int(input()))

# cost = []
for i in range(order_num):
    # cost.append(int(input()))
    c = int(input())
    index = tableno[i]
    res[index-1] += c

max_cost = max(res)
for i in range(len(res)):
    if res[i] == max_cost:
        print(i+1)
