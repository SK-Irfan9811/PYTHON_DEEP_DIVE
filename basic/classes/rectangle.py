class Rectangle:
    def __init__(self, height, width):
        """
        we are using setters for instantiation of values
        :param height:
        :param width:
        """
        self.height = height  # self.height is our height setter
        self.width = width  # self.width is our height setter

    @property
    def width(self):
        print("getting width")
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
        return self._height * self._width

    def perimeter(self):
        return 2 * (self._width + self._height)

    def set_width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError('Width can not be -ve')

    def get_width(self):
        return self._width

    def set_height(self, height):
        if height > 0:
            self._height = height
        else:
            raise ValueError('Height can not be -ve')

    def get_height(self):
        return self._height

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

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = Rectangle(20, 30)

# print(r1 == r2, r1 is r2)
# print(r1 < r3)
# print(r3 > r2)
r1.width = 2020
r1.height = 2020
# print(r1)
# r4 = Rectangle(-100, -200) raises error
