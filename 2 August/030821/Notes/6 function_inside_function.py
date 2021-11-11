
def generate_function():
    def even_odd(val):
        if val % 2 == 0:
            return True
        else:
            return False
    return even_odd


test_function = generate_function()
print(test_function(10))
