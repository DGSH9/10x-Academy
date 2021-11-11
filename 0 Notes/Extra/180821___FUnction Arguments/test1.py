def area(radius,pi):
    return pi*radius*radius

radius = 5
pi=3.14
# print(area(radius,pi))          # default argument
# print(area(pi,radius))          #-->give wrong answer due to argument
# print(area(pi=10,radius=1000))  #-->keyword argument
def printStudentname1(*args):     # single * is for tuple
    for n in args:
        print(n)

def printStudentName2(**args):    # double ** used to create dictionary
    for k,v in args.items():
        print(k)
        print(v)

printStudentName2(name ='durgesh',surname='yadav',name2='pritam',surname2='singh')
# name ='durgesh',
# surname='yadav',
# name2='pritam',  
# surname2='singh'