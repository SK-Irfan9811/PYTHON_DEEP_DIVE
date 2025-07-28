"""
Note - Even the callables are still class attributes, the only change is their value is of different type...
So we can access that callable(assume - a static function) from the dot notation approach,getattr() and using __dict__(not recommended though)
"""


class MyCar:
    brand = "Jaguar"
    model = "F-Type"

    def drive():
        print(f"zui zuiii - {MyCar.brand}")

print(isinstance(MyCar,type))
# print(MyCar.__dict__)
# MyCar.__dict__["drive"]()
# getattr(MyCar, "drive")()
# MyCar.drive()
