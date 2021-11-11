# This function should return a function which takes string as input
# removes all the alphabets which are present in the forbidden_alphabets list
# forbidden_alphabets is a list off alphabets
# Your returned function should take string as input returns a string
# by removing forbidden alphabets
def word_smith(forbidden_alphabets):
    # You can start from her
    def f2(s):
        # remove your alphabets
        temp = ""
        for character in s:
            if character not in forbidden_alphabets:
                temp += character
        return temp
    return f2


# Do not change anything below this line.
if __name__ == "__main__":
    alphabets = [i for i in input().split(' ')]
    input_string = input()
    chopper = word_smith(alphabets)
    print(chopper(input_string))
