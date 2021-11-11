# Your class should be named as `Rectangle`.
# Method to get area should be named as `rectangle_area`.
# Method to get perimeter should be named as `rectangle_perimeter`.
# You should be taking `length` and `width` as inputs when creating the object for your class.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        if self.length > 0 and self.width > 0:
            return (self.length*self.width)
        else:
            return 0

    def rectangle_perimeter(self):
        if self.length > 0 and self.width > 0:
            return 2*(self.length+self.width)
        else:
            return 0


if __name__ == "__main__":
    newRectangle = Rectangle(int(input()), int(input()))
    print(newRectangle.rectangle_area())
    print(newRectangle.rectangle_perimeter())
