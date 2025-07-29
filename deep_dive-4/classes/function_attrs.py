"""Unlike data attributes functions in the classes(methods) behave differently.
When we call a method through a object, then the first param is that object itself.
So that we can have a handle of that particular object's namespace.
"""


class MyCar:
    top_speed = 200
    brand = "BMW"

    def accelerate(self):
        self.top_speed += 30
        print(f"{self.brand} is cruising at {self.top_speed}")

    def decelerate(self):
        self.top_speed -= 10
        print(f"{self.brand} is slowing down... {self.top_speed}")


porsche = MyCar()
# below are equivalent
porsche.brand = "porsche"
porsche.top_speed = 300
# porsche.decelerate = lambda self: print(f"{self.brand} is slowing down... {self.top_speed - 30}")
porsche.accelerate()
porsche.accelerate()
porsche.accelerate()
porsche.decelerate()
porsche.decelerate()
porsche.decelerate()
# porsche.decelerate(porsche)
# print(porsche.decelerate)
# print(porsche.accelerate)
MyCar.accelerate(MyCar)
