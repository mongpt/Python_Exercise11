
#11.1
class publications:
    def __init__(self, name):
        self.name = name

    def print(self, *args):
        listAttributes = []
        for i in args:
            listAttributes.append(i)
        if len(listAttributes) == 2:
            print(f"{listAttributes[0]} (chief editor {listAttributes[1]})")
        else:
            print(f"{listAttributes[0]} (author {listAttributes[1]}, {listAttributes[2]} pages)")


class book(publications):
    def __init__(self, name, author, page):
        super().__init__(name)
        self.author = author
        self.page = page

    def print_information(self):
        print("\nBook information: ")
        super().print(self.name, self.author, self.page)


class magazine(publications):
    def __init__(self, name, chiefEditor):
        super().__init__(name)
        self.chiefEditor = chiefEditor

    def print_information(self):
        print("\nMagazine information: ")
        super().print(f"'{self.name}'", f"'{self.chiefEditor}'")


print("\n****** Exercise 11.1 ******")
newMagazine = magazine("Donald Duck","Aki Hyyppä")
newBook = book("Compartment No. 6", "Rosa Liksom", 192)

newMagazine.print_information()
newBook.print_information()

#11.2

class car:
    def __init__(self, regNumber, maxSpeed):
        self.regNum = regNumber
        self.maxSpeed = maxSpeed
        self.curSpeed = 0
        self.travelledDistance = 0

    def accelerate(self, speed):
        self.curSpeed += speed
        if self.curSpeed < 0:
            self.curSpeed = 0
        elif self.curSpeed > self.maxSpeed:
            self.curSpeed = self.maxSpeed
        return self.curSpeed

    def drive(self, hours):
        self.travelledDistance += self.curSpeed * hours
        return self.travelledDistance


class ElectricCar(car):
    def __init__(self, regNumber, maxSpeed, battCap):
        super().__init__(regNumber, maxSpeed)
        self.battCap = battCap


class GasolineCar(car):
    def __init__(self, regNumber, maxSpeed, tankVol):
        super().__init__(regNumber, maxSpeed)
        self.tankVol = tankVol


print("\n****** Exercise 11.2 ******")
newEcar = ElectricCar("ABC-15", 180, 52.5)
newEcar.accelerate(80)
newEcar.drive(3)
print(f"Electric car travelled: {newEcar.travelledDistance} km")
newGcar = GasolineCar("ACD-123", 165, 32.3)
newGcar.accelerate(120)
newGcar.drive(3)
print(f"Gasoline car travelled: {newGcar.travelledDistance} km")
