n = int(input())                         #7
arr1 = list(map(int,input().split()))    #9 8 -10 8 7 -6 1
arr1.sort()                              #-10 -6 0 7 8 8 9

left = 0                                 #0 =>0 =>0 =>0 =>0 =>0 =>0
right = len(arr1)-1                      #6 =>5 =>4 =>3 =>2 =>1 =>0
left_val = None                          #None => -10
right_val = None                         #None => 9

mini = float('inf')                      #... => 1

while(left < right):                      
    diff = arr1[left] + arr1[right]      # 1 => 2 => 2 => 3 => 10 => 16
    if(abs(diff) < mini):                # True => False =>False =>False =>False =>False
        mini = abs(diff)                  
        left_val = arr1[left]
        right_val = arr1[right]

    if diff == 0:
        break
    if diff < 0:                        #False =>False>......................
        left+=1
    else:
        right-=1                        #True => True =>True =>True =>True =>True


print(left_val,right_val,mini)
# -10,9,1