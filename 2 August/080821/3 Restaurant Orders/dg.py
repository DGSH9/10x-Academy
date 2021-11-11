#Restaurant Orders

n = int(input())        #1, 1
t = int(input())        #1, 1
cost = [0]*t            #n, n
tb = []                 #1, n
for i in range(n):      #=>n, n  (time and space for loop this)
	x = int(input())     
	tb.append(x)        
for i in range(n):      #=>n, n  (time and space for loop this)
	x = int(input())    
	cost[tb[i]-1]+=x    
mx = max(cost)          #n, 1
for i in range(t):      #n, 0    (time and space for loop this)
	if(cost[i]==mx):   
		print(i+1)     

# total time = O(n) + O(n) + O(n) = O(3*n) => O(n)
# total space = O(n)