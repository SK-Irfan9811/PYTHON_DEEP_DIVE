class Rectangle:
    def __init__(self, height, width):
        """
        we are using setters for instantiation of values
        :param height:
        :param width:
        """
        self.height = height  # self.height is our height setter
        self.width = width  # self.width is our width setter

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be +ve')
        else:
            self._width = width

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be +ve')
        else:
            self._height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return "Rectangle : {0} {1}".format(self._height, self._width)

    def __repr__(self):
        return "Rectangle({},{})".format(self._height, self._width)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self._width, self._height) == (other._width, other._height)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = Rectangle(20, 30)

print(r1 == r2, r1 is r2)
print(r1 < r3)
print(r2 > r3)
r1.width = 2024
r1.height = 2024
print(r1.area(), r1.perimeter())
print(str(r1))
print(repr(r1))
# r4 = Rectangle(-100, -200)  #raises error
