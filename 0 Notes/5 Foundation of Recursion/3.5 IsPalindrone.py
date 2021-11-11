def isPalindrone(word):
    if(len(word) <= 1):
        return True
    else:
        if(word[0] == word[-1]):
            return isPalindrone(word[1:-1])
        else:
            return False


d = 'CIVIC'
print(isPalindrone(d))
