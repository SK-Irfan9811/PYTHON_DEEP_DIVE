from functools import reduce

london = ("London", "UK", 2000_2000)
newyork = ("Newyork", "USA", 300_000)
beijing = ("Beijing", "China", 9000_9000)

cities = [london, newyork, beijing]
total_pop = reduce(lambda initial, c: initial + c[2], cities, 0)
print(total_pop)

# unpacking
record = ("Irfan", 2002, "FEB", 5, 23)
name, *_, age = record
print(name, age, _)  # _ is dummy variable to indicate that is has the least importance


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({0},{1})".format(self.x, self.y)


point1 = (Point2D(100, 200), Point2D(300, 400))
print(point1)
point1[0].y = -1
print(point1)

p1 = (0, 0)
p2 = (100, 200)
print([*p1, *p2])

# enumerate
for idx, city in enumerate(cities):
    print(idx, city)
