def isPalindrone(word):
    if(len(word) <= 1):
        return True
    else:
        if(word[0] == word[-1]):
            return isPalindrone(word[1:-1])
        else:
            return False


print(isPalindrone('RACECAR'))


# Recursive Function = f(n) = len(word)-(n-1)
# Base function = len(word) <= 1
#
# start at index 1
# 1 == n
# 2 == n-1
# 3 == n-2
# ........
# n == 1

# total time = branch *height = 1*n/2 = O(n/2) => O(n)
