## Following function takes integer and should return True if it's prime 
## otherwise  should return False.
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

### Please don't change anything below this line.
if __name__ == "__main__":
    number = int(input())
    print(is_prime(number))