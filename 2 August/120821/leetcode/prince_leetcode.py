n = int(input())
for _ in range(n):   
    count1 = 0                         
    arr = list(map(int,input().split())) 
    arr.sort()
    x,y,z,r = arr[0],arr[1],arr[2],arr[3]
    
    if((x!=y and z!=r) and (x!=z) and (y!= r)):
        count1=2
    elif((x==y and z==r)):
        if(y!=z and (x!=r)):
            count1=2
    elif((x!=y and z==r)):
        if((x!=z) and y==r):
            count1=1
    print(count1)