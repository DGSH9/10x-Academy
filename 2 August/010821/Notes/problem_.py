"""
dimensions of bricks now calculate volume of bricks

length = 20
width = 10
height = 5
"""


def bricks_volume(length=20, width=10, height=5):  # called taking default value
    print('Default length is :', length)
    print('Default width is :', width)
    print('Default height is :', height)
    return length*width*height

print(bricks_volume(width=50))

# we are taking different quantity of bricks
# Taking input as quantity
def bricks_volume(quantity, length=20, width=10, height=5):  # called taking default value
    print('Enter quantity :', quantity)
    print('Default length is :', length)
    print('Default width is :', width)
    print('Default height is :', height)
    return quantity*length*width*height


quantity = input()
print(bricks_volume(int(quantity)))                          # This is the way we are calling the functions        #
