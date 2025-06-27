# getattr function
class MyCar:
    brand = "BMW"
    model = "M5"


print(getattr(MyCar, "brand"))
# print(getattr(MyCar,"engine"))
print(getattr(MyCar, "engine", "N/A"))

# setattr function
setattr(MyCar, "engine", "v12")
setattr(MyCar, "model", "M5 Competition")
MyCar.type = "petrol"
print(MyCar.type, MyCar.model, MyCar.engine)

# delattr
print(MyCar.__dict__,type(MyCar.__dict__))
delattr(MyCar, "engine")
print(MyCar.__dict__)
del MyCar.type
print(MyCar.__dict__)
