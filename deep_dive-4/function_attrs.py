class MyCar:
    top_speed = 200
    brand = "BMW"

    def accelerate(self):
        print(f"{self.brand} is cruising at {self.top_speed + 30}")


porsche = MyCar()
# below are equivalent
porsche.brand = "porsche"
porsche.top_speed = 300
porsche.decelerate = lambda self: print(f"{self.brand} is slowing down... {porsche.top_speed - 60}")
porsche.accelerate()
porsche.decelerate(porsche)
print(porsche.decelerate)
print(porsche.accelerate)
MyCar.accelerate(MyCar)
