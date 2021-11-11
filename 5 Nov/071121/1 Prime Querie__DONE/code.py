# https://6793fdf6.widgets.sphere-engine.com/lp?hash=cL2ytmwX2P

# https://6793fdf6.widgets.sphere-engine.com/lp?hash=cL2ytmwX2P
# 041021
# 021121
# solution  = 5 oct
""""
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
0,1,1,0,1,0,1,0,0,0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0

1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 

make a result array which denote 0 = not prime
                                 1 = prime number
every composite number ,has prime number as its factor
approach called ==>sieve of eratosthenes =>prime number upto n

"""


n,q = map(int,input().split())
prime_number = [1 for i in range(n+1)] #remember to start with zero

prime_number[0],prime_number[1] = 0, 0

p = 2 #start from two upto end
while p*p <=n:
    if prime_number[p] == 1:
        for i in range(p*p,n+1,p):
            prime_number[i] = 0
    
    p+=1

#for cumulative sum
for i in range(1,len(prime_number)):
    prime_number[i] +=prime_number[i-1]
for i in range(q):
    query = int(input())
    print(prime_number[query])