"""
Principle amount(p)= 1000
Time            (t)= 10
Rate            (r)= 5


SI = (p x t x r)/100
Output = 500

Input:->
        p = 1000        ->int
        t = 10          ->int
        r = 5           ->int

Process->
        SI = (p*t*r)/100  =>(1000 x 10 x 5)/100 =>500
        
Output->
        500

"""
p = int(input())
t = int(input())
r = int(input())

Si = int((p*t*r)/100)

print(Si)