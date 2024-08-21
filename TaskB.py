class Seats:
    def __init__(self, Nos, col, mov):
        self.NumberofSeats = Nos
        self.Colour = col
        self.Movement = mov

    def display_specification_seats(self):
        print("Seat Specification")
        print(f"Number of Seats in Car : {self.NumberofSeats}")
        print(f"Seat Colour : {self.Colour}")
        print(f"Movement of seats : {self.Movement}")


class Engine:
    def __init__(self, EnTyp, Hp, fultyp):
        self.EngineType = EnTyp
        self.HorsePower = Hp
        self.FuelType = fultyp

    def display_specification_engine(self):
        print("Engine Specification")
        print(f"Engine Type  : {self.EngineType}")
        print(f"Generates HorsePower of  : {self.HorsePower}")
        print(f"Fuel Type : {self.FuelType}")


class Doors:
    def __init__(self, NoD, Dtyp):
        self.numberofdoor = NoD
        self.DoorType = Dtyp

    def display_specification_Door(self):
        print("Door Specification")
        print(f"Number of doors : {self.numberofdoor}")
        print(f"Door Type : {self.DoorType}")


class Multimedia:
    def __init__(self, Scsiz, Typ, spek):
        self.ScreenSize = Scsiz
        self.Software = Typ
        self.Speaker = spek

    def display_specification_Multimedia(self):
        print("Multimedia Specification")
        print(f"Multimedia screen size : {self.ScreenSize}")
        print(f"Multimedia Software : {self.Software}")
        print(f"Speakers : {self.Speaker}")


class Suspension:
    def __init__(self, sustyp, sptyp):
        self.SuspensionType = sustyp
        self.SpringType = sptyp

    def display_specification_Suspension(self):
        print("Suspension Specification")
        print(f"Suspension Type : {self.SuspensionType}")
        print(f"Spring Type : {self.SpringType}")


class ElectricalSystem:
    def __init__(self, bc, v):
        self.BatteryCapacity = bc
        self.voltage = v

    def display_specification_electricsystem(self):
        print("Electrical System Specification")
        print(f"Battery Capacity : {self.BatteryCapacity}")
        print(f"Voltage : {self.voltage}")


class Car:
    def __init__(self, Nos=4, col="Black", mov="Manual", EnTyp="Petrol", Hp=150, fultyp="Petrol", NoD=4, Dtyp="Standard",
                 Scsiz="7-inch", Typ="Basic", spek=4, sustyp="Standard", sptyp="Coil", bc="50 kWh", v="12V"):
        self.seat = Seats(Nos, col, mov)
        self.engine = Engine(EnTyp, Hp, fultyp)
        self.door = Doors(NoD, Dtyp)
        self.multimedia = Multimedia(Scsiz, Typ, spek)
        self.suspension = Suspension(sustyp, sptyp)
        self.electricsystem = ElectricalSystem(bc, v)

    def display(self):
        self.engine.display_specification_engine()
        self.door.display_specification_Door()
        self.seat.display_specification_seats()
        self.multimedia.display_specification_Multimedia()
        self.suspension.display_specification_Suspension()
        self.electricsystem.display_specification_electricsystem()

    def __str__(self):
         return (f"Car Specifications:\n"
            f"- Seats: {self.seat.NumberofSeats} {self.seat.Colour}, Movement: {self.seat.Movement}\n"
            f"- Engine: {self.engine.HorsePower} HP, Type: {self.engine.EngineType}, Fuel: {self.engine.FuelType}\n"
            f"- Doors: {self.door.numberofdoor} {self.door.DoorType}\n"
            f"- Multimedia: {self.multimedia.ScreenSize} screen, Software: {self.multimedia.Software}, Speakers: {self.multimedia.Speaker}\n"
            f"- Suspension: {self.suspension.SuspensionType}, Spring Type: {self.suspension.SpringType}\n"
            f"- Electrical System: Battery Capacity: {self.electricsystem.BatteryCapacity}, Voltage: {self.electricsystem.voltage}")



class CarFactory:
    _instance = None
    _produced_cars = []

    def __init__(self):
        raise RuntimeError("This is a Singleton class, use get_instance() instead.")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    def create_car(self, Nos=4, col="Black", mov="Manual", EnTyp="Petrol", Hp=150, fultyp="Petrol", NoD=4, Dtyp="Standard",
                   Scsiz="7-inch", Typ="Basic", spek=4, sustyp="Standard", sptyp="Coil", bc="50 kWh", v="12V"):
        car = Car(Nos, col, mov, EnTyp, Hp, fultyp, NoD, Dtyp, Scsiz, Typ, spek, sustyp, sptyp, bc, v)
        self._produced_cars.append(car)
        return car

    def get_produced_cars(self):
        car_counts = {}
        for car in self._produced_cars:
            car_str = str(car)
            if car_str in car_counts:
                car_counts[car_str] += 1
            else:
                car_counts[car_str] = 1
        return car_counts



# Example usage
factory = CarFactory.get_instance()


car1 = factory.create_car()


car2 = factory.create_car(Nos=2, col="Red", mov="Automatic", EnTyp="Electric", Hp=250, fultyp="Electric")

# Display the cars
car1.display()
print("\n")
car2.display()


produced_cars = factory.get_produced_cars()
for car, count in produced_cars.items():
    print(f"{car}: {count} produced ")
    print("\n")
