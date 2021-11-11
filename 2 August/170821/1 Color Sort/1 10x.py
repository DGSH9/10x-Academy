n = int(input())
arr1 = []
for i in range(n):
    arr1.append(int(input()))
count_colors = [0,0,0]
for i in arr1:
    count_colors[i] +=1

for i in range(n):
    if(i<count_colors[0]):
        arr1[i] = 0
    elif(i<(count_colors[0]+count_colors[1])):
        arr1[i] = 1
    else:
        arr1[i]=2    
[print(i) for i in arr1]