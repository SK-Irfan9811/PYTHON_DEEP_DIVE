class MyCar:
    brand = "Jaguar"
    model = "F-Type"

    def drive():
        print(f"zui zuiii")


print(MyCar.__dict__)
MyCar.__dict__["drive"]()
getattr(MyCar,"drive")()
MyCar.drive()
