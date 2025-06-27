class Car:
    # __class__=str
    brand = "BMW"
    model = "M5"


print(Car.__dict__)

jaguar = Car()
jaguar.brand = "Jaguar"
jaguar.model = "F-Type"
print(jaguar.__dict__)

toyota = Car()
toyota.brand = "toyota"
toyota.model = "supraaaa"
print(toyota.__dict__)

print(toyota.__class__)
