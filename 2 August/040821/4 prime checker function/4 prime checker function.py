# Following function takes integer and should return True if it's prime
# otherwise  should return False.
def is_prime(input_number):
    if input_number > 1:
        for i in range(2, int(input_number/2)+1):
            if (input_number % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False


# Please don't change anything below this line.
if __name__ == "__main__":
    number = int(input())
    print(is_prime(number))
