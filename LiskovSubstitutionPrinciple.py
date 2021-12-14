# objects of a superclass shall be replaceable with objects of its subclasses without breaking the application
# It Is broken in the below example
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._height * self._width

    def __str__(self):
        return f"Width: {self.width} Height: {self.height}"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc1):
    w = rc1.width
    rc1.height = 10
    expected = int(w * 10)
    print(f"Expected an area of {expected}, got {rc1.area}")


if __name__ == '__main__':
    rc = Rectangle(3, 4)
    use_it(rc)
    sq = Square(5)
    use_it(sq)