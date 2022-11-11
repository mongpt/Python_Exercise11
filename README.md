# Python_Exercise11
## 11. Inheritance

1. Implement the following class hierarchy using Python: A publication can be either a book or a magazine. Each publication has a name. Each book 
also has an author and a page count, whereas each magazine has a chief editor. Also write the required initializers to both classes. Create a 
`print_information` method to both subclasses for printing out all information of the publication in question. In the main program, create 
publications Donald Duck (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information of both
publications using the methods you implemented. 
```python
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
```
Output console:
```
****** Exercise 11.1 ******

Magazine information: 
'Donald Duck' (chief editor 'Aki Hyyppä')

Book information: 
Compartment No. 6 (author Rosa Liksom, 192 pages)
```

2. Extend the previosly written `Car` class by adding two subclasses: `ElectricCar` and `GasolineCar`. Electric cars have the capacity of the 
battery in kilowatt-hours as their property. Gasoline cars have the volume of the tank in liters as their property. Write initializers for the
subclasses. For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity as its parameter.
It calls the initializer of the base class to set the first two properties and then sets its capacity. Write a main program where you create
one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars, make them drive for
three hours and print out the values of their kilometer counters.
```python
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
```
Output console:
```
****** Exercise 11.2 ******
Electric car travelled: 240 km
Gasoline car travelled: 360 km
```
