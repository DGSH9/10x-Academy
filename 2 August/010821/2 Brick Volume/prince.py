# You should fill this functions using the volume and calculate_price functions defined below this.
# dimensions is a list with 2 values width and height respectively
# brick_count is int representing total bricks
def calculate_total_price_of_bricks(dimensions, brick_count):
    w, h = dimensions
    if(w == -1):
        w = 60
    if(h == -1):
        h = 40
    return calculate_price(volume(length=100, width=w, height=h)*brick_count)
    
# Do not 1change anything below this line
def volume(length=100, width=60, height=40):
    return length*width*height


def calculate_price(volume, price=0.00005):
    return round(volume*price)


if __name__ == "__main__":
    brick_count = int(input())
    dimensions = [int(i) for i in input().split(' ')]
    total_price = calculate_total_price_of_bricks(dimensions, brick_count)
    print(total_price)
