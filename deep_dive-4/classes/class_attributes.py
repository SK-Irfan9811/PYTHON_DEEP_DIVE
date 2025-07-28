"""
Note: So we have 3 inbuilt functions to work on attrs.
1. getattr(object,attr_name: str,default_value: Any (if attr is absent - basically suppresses the 'AttributeError Exception') or dot notation
2. setattr(object,attr_name: str,attr_value: Any) or dot notation
3. delattr(object,attr_name: str) or del keyword

"""


# getattr function
class MyCar:
    brand = "BMW"
    model = "M5"


print(getattr(MyCar, "brand"))
# print(getattr(MyCar,"engine")) throws AttributeError exception.
print(getattr(MyCar, "engine", "N/A"))
print(getattr(MyCar(), "brand"))

# setattr function
setattr(MyCar, "engine", "v12")
setattr(MyCar, "model", "M5 Competition")
MyCar.type = "petrol"
print(MyCar.__dict__)
print(MyCar.type, MyCar.model, MyCar.engine)

# delattr
print(MyCar.__dict__, type(MyCar.__dict__))
delattr(MyCar, "engine")
print(MyCar.__dict__)
del MyCar.type
print(MyCar.__dict__)
