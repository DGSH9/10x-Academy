

q = int(input())
for i in range(q):
        def is_prime(input_number):
    # You can start below this
            count=0
            for i in range(1,input_number+1):
                if(input_number%i==0):
                    count+=1
            if(count==2):
                return True
            elif(count==1):
                return False
            else:
                return True
	x = int(input())
	p_count = 0
	for j in range(x):
        if (is_prime(j) == True):
            p_count+=1
        

